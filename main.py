import multiprocessing
import os
import shutil
import tempfile
from pathlib import Path

import streamlit as st
import torch
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    AcceleratorOptions,
    EasyOcrOptions,
    PdfPipelineOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption
from dotenv import load_dotenv

from src.utils.logger_config import logger


def get_converter(ocr: bool = False):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    logger.info(f"Using device: {device} | OCR mode: {ocr}")

    pipeline_options = PdfPipelineOptions(
        do_table_structure=False,
        do_ocr=ocr,
        **(
            {"ocr_options": EasyOcrOptions(lang=["fr", "en"], force_full_page_ocr=True)}
            if ocr
            else {}
        ),
        images_scale=1.0,
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


@st.cache_resource
def get_native_converter():
    return get_converter(ocr=False)


@st.cache_resource
def get_ocr_converter():
    return get_converter(ocr=True)


def pdf_to_text(pdf_path, converter):

    result = converter.convert(pdf_path)
    doc = result.document

    # Pages
    logger.info(f"Total pages: {len(result.pages)}")

    # Pictures
    logger.info(f"Total pictures detected: {len(doc.pictures)}")
    for i, pic in enumerate(doc.pictures):
        logger.info(f"Picture {i} - Caption: {pic.caption_text(doc)}")

    # TODO: Add image OCR

    text = doc.export_to_text()
    logger.info(f"Extracted text from {pdf_path}")
    return text


if __name__ == "__main__":

    # Initialize session state and logging
    if "initialized" not in st.session_state:
        # Set up logging
        logger.info("Starting the Simple RAG application...")

        # Prepare directories
        COPIED_DIR = Path("outputs/copied_pdfs")
        OUTPUT_DIR = Path("outputs/ocr_outputs")

        COPIED_DIR.mkdir(exist_ok=True, parents=True)
        OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
        logger.info(f"Created directories: {COPIED_DIR}, {OUTPUT_DIR}")

        # Load environment variables
        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        logger.info("Loaded environment variables.")

        # Store in session state
        st.session_state["COPIED_DIR"] = COPIED_DIR
        st.session_state["OUTPUT_DIR"] = OUTPUT_DIR
        st.session_state["parsing_results"] = {}
        st.session_state["initialized"] = True

    # Initialize converters
    native_converter = get_native_converter()
    ocr_converter = get_ocr_converter()
    if "converters_logged" not in st.session_state:
        logger.info("Initialized document converters.")
        st.session_state["converters_logged"] = True

    # Streamlit UI
    st.set_page_config(page_title="Simple RAG", layout="wide")
    st.title("📄 Simple RAG")

    uploaded_files = st.file_uploader(
        "Upload PDF", type="pdf", accept_multiple_files=True
    )

    # Upload and process PDFs
    if uploaded_files:

        # TODO: This is a temporary fix, scanned file detection will be implemented
        #  in the future
        # Scanned PDF checkboxes
        scanned_map = {}
        for uploaded_file in uploaded_files:
            scanned_map[uploaded_file.name] = st.checkbox(
                f"Is {uploaded_file.name} a scanned PDF?", key=uploaded_file.name
            )

        if st.button("Process PDF files"):

            with tempfile.TemporaryDirectory() as tmpdir:
                for uploaded_file in uploaded_files:
                    filename = Path(uploaded_file.name).stem
                    file_id = f"{uploaded_file.name}_{uploaded_file.size}"

                    # Skip if already processed in this session
                    if file_id in st.session_state["parsing_results"]:
                        continue

                    st.write(f"📄 Processing file: {filename}")
                    logger.info(f"Processing file: {filename}")

                    temp_path = Path(tmpdir) / uploaded_file.name
                    temp_path.write_bytes(uploaded_file.getbuffer())

                    # Copy PDF to copied_pdfs directory
                    copied_path = st.session_state["COPIED_DIR"] / uploaded_file.name
                    shutil.copy(temp_path, copied_path)
                    logger.info(f"Copied {uploaded_file.name} to {copied_path}")

                    # Check whether the file is a native PDF or scanned PDF
                    is_scanned = scanned_map[uploaded_file.name]
                    logger.info(f"Is {uploaded_file.name} a scanned PDF? {is_scanned}")

                    if not is_scanned:
                        # Native PDF
                        with st.spinner(
                            f"Extracting text from {uploaded_file.name}..."
                        ):
                            text = pdf_to_text(
                                pdf_path=str(temp_path), converter=native_converter
                            )
                            logger.info(
                                f"Text extraction completed for {uploaded_file.name}"
                            )
                    else:
                        # OCR
                        with st.spinner(f"OCR on {uploaded_file.name}..."):
                            text = pdf_to_text(
                                pdf_path=str(temp_path), converter=ocr_converter
                            )
                            logger.info(f"OCR completed for {uploaded_file.name}")

                    # Save in Markdown format
                    output_path = st.session_state["OUTPUT_DIR"] / f"{filename}.md"
                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write(text)
                    logger.info(f"Saved Markdown file: {output_path}")
                    st.success(f"Processed {uploaded_file.name} and \
                          saved as {output_path.name}")

                    # Update session state with parsing results
                    st.session_state["parsing_results"][file_id] = {
                        "filename": filename,
                        "text": text,
                        "path": str(output_path),
                        "is_scanned": is_scanned,
                    }

            st.success("All done! You can find the processed Markdown files in\
                      the 'outputs/ocr_outputs' directory.")
            logger.info("All files processed successfully.")
