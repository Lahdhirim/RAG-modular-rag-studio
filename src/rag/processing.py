import hashlib
import multiprocessing
import os
import tempfile
import uuid

import fitz
import torch
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    AcceleratorOptions,
    EasyOcrOptions,
    PdfPipelineOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.utils.logger_config import logger


def get_converter(ocr: bool = False):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    logger.info(f"Using device: {device} | OCR mode: {ocr}")

    pipeline_options = PdfPipelineOptions(
        do_table_structure=True,
        do_ocr=ocr,
        **(
            {"ocr_options": EasyOcrOptions(lang=["fr", "en"], force_full_page_ocr=True)}
            if ocr
            else {}
        ),
        images_scale=1,
        generate_page_images=True,
        generate_picture_images=True,
        accelerator_options=AcceleratorOptions(
            num_threads=multiprocessing.cpu_count(), device=device
        ),
    )

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    return converter


def pdf_to_text(pdf_path, converter):
    doc = fitz.open(pdf_path)

    full_text = ""
    total_pages = len(doc)

    logger.info(f"Total pages detected: {total_pages}")

    for i in range(total_pages):
        logger.info(f"Processing page {i+1}/{total_pages}")

        single_page_doc = fitz.open()
        single_page_doc.insert_pdf(doc, from_page=i, to_page=i)

        temp_path = None
        try:
            temp_path = os.path.join(
                tempfile.gettempdir(), f"page_{i}_{uuid.uuid4().hex}.pdf"
            )
            single_page_doc.save(temp_path)
            single_page_doc.close()

            result = converter.convert(temp_path)
            docling_doc = result.document

            page_text = docling_doc.export_to_text()

            full_text += f"\n\n--- Page {i+1} ---\n\n{page_text}"

        except Exception as e:
            logger.error(f"Error on page {i+1}: {e}")

        finally:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except Exception as e:
                    logger.warning(f"Could not delete temp file {temp_path}: {e}")

        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    doc.close()
    return full_text


def generate_file_id(uploaded_file):
    file_bytes = uploaded_file.getbuffer()
    return hashlib.sha256(file_bytes).hexdigest()


def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_text(text)
