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

from src.config_loader import ParsingConfig, RAGConfig
from src.utils.logger_config import logger, processing_job_logger
from src.utils.schema import ChunksSchema, ParsingSchema


def get_converter(parsing_config: ParsingConfig, ocr: bool = False):
    device = (
        "cuda" if (torch.cuda.is_available() and parsing_config.enable_gpu) else "cpu"
    )
    logger.info(f"Using device: {device} | OCR mode: {ocr}")

    parser_name, parser_cfg = parsing_config.get_selected_parser()
    logger.info(f"Selected parsing method: {parser_name} with config: {parser_cfg}")

    if parser_name == ParsingSchema.DOCLING:
        selected_languages = (
            parser_cfg.params.get("languages", ["en", "fr"])
            if parser_cfg.params
            else ["en", "fr"]
        )

        pipeline_options = PdfPipelineOptions(
            do_table_structure=True,
            do_ocr=ocr,
            **(
                {
                    "ocr_options": EasyOcrOptions(
                        lang=selected_languages, force_full_page_ocr=True
                    )
                }
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

    else:
        logger.error(f"Unsupported parsing method: {parser_name}")
        raise ValueError(f"Unsupported parsing method: {parser_name}")


def pdf_to_text(pdf_path, converter):
    doc = fitz.open(pdf_path)

    full_text = ""
    total_pages = len(doc)

    processing_job_logger.info(f"Total pages detected: {total_pages}")

    successfully_processed_pages, failed_pages = 0, 0

    for i in range(total_pages):
        processing_job_logger.info(f"Processing page {i+1}/{total_pages}")

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
            successfully_processed_pages += 1

        except Exception as e:
            processing_job_logger.error(f"Error on page {i+1}: {e}")
            failed_pages += 1

        finally:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except Exception as e:
                    processing_job_logger.warning(
                        f"Could not delete temp file {temp_path}: {e}"
                    )

        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    doc.close()
    processing_job_logger.info(
        f"Processed pages: {successfully_processed_pages}, Failed pages: {failed_pages}"
    )
    return full_text, successfully_processed_pages, failed_pages


def generate_file_id(uploaded_file):
    file_bytes = uploaded_file.getbuffer()
    return hashlib.sha256(file_bytes).hexdigest()


def get_chunker(chunking_config: RAGConfig):
    chunker_name, chunker_cfg = chunking_config.get_selected_chunker()
    logger.info(f"Selected chunking method: {chunker_name} with config: {chunker_cfg}")

    if chunker_name == ChunksSchema.RECURSIVE_CHARACTER:
        return RecursiveCharacterTextSplitter(
            chunk_size=chunker_cfg.params.get("chunk_size", 500),
            chunk_overlap=chunker_cfg.params.get("chunk_overlap", 50),
        )

    else:
        logger.error(f"Unsupported chunking method: {chunker_name}")
        raise ValueError(f"Unsupported chunking method: {chunker_name}")
