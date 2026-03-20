import hashlib
import multiprocessing
import os
import shutil
import tempfile
import uuid
from pathlib import Path

import fitz
import numpy as np
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
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config_loader import load_config
from src.utils.logger_config import logger


def generate_file_id(uploaded_file):
    file_bytes = uploaded_file.getbuffer()
    return hashlib.sha256(file_bytes).hexdigest()


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


@st.cache_resource
def get_native_converter():
    return get_converter(ocr=False)


@st.cache_resource
def get_ocr_converter():
    return get_converter(ocr=True)


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


def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_text(text)


@st.cache_resource
def get_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def embed_chunks(chunks):
    model = get_embeddings()

    # TODO: Add Schema (state and chunks)
    texts = [c["text"] for c in chunks]

    vectors = model.embed_documents(texts)

    matrix = np.array(vectors)
    matrix = matrix / np.linalg.norm(matrix, axis=1, keepdims=True)

    return matrix


def embed_query(query):
    model = get_embeddings()
    vec = np.array(model.embed_query(query))
    return vec / np.linalg.norm(vec)


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

        # Load configuration
        config_path = Path("config/config.json")
        config = load_config(config_path)
        logger.info(f"Loaded configuration from {config_path}: {config}")

        # Store in session state
        st.session_state["config"] = config
        st.session_state["COPIED_DIR"] = COPIED_DIR
        st.session_state["OUTPUT_DIR"] = OUTPUT_DIR
        st.session_state["parsing_results"] = {}
        st.session_state["vector_store"] = {"chunks": [], "matrix": None}
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
                    file_id = generate_file_id(uploaded_file)

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

                    # Chunking
                    chunks = chunk_text(text)
                    logger.info(
                        f"Chunked text into {len(chunks)} chunks for {uploaded_file.name}"
                    )
                    chunks_with_metadata = [
                        {"text": chunk, "source": filename} for chunk in chunks
                    ]
                    st.session_state["vector_store"]["chunks"].extend(
                        chunks_with_metadata
                    )

                    # Update session state with parsing results
                    st.session_state["parsing_results"][file_id] = {
                        "filename": filename,
                        "text": text,
                        "path": str(output_path),
                        "is_scanned": is_scanned,
                    }

            st.success("All done! You can now ask questions about your documents.")
            logger.info("All files processed successfully.")

    # Embedding and similarity search
    if st.session_state["vector_store"]["chunks"]:
        all_chunks = st.session_state["vector_store"]["chunks"]
        matrix = embed_chunks(all_chunks)
        st.session_state["vector_store"]["matrix"] = matrix
        logger.info(
            f"Embedded {len(all_chunks)} chunks into vector store with shape {matrix.shape}."
        )

    if st.session_state["vector_store"]["matrix"] is not None:
        matrix = st.session_state["vector_store"]["matrix"]

        query = st.text_input("Ask your question here:")
        if query:
            logger.info(f"Received query: {query}")
            query_vec = embed_query(query)

            # Compute cosine similarity
            similarities = matrix @ query_vec

            # Get top k most relevant chunks and filter by similarity threshold
            best_indexes = np.argsort(similarities)[-5:]
            filtered_indexes = [
                best_index
                for best_index in best_indexes
                if similarities[best_index] > 0.5
            ]
            logger.info(
                f"Best matching chunk indexes: {best_indexes} with respective similarities: {similarities[best_indexes]}, filtered indexes: {filtered_indexes}"
            )

            top_chunks = [all_chunks[i] for i in filtered_indexes]
            logger.info(f"Top chunks: {top_chunks}")

            # Display results
            st.write("### Top relevant chunks:")
            for chunk in top_chunks:
                st.write(f"- {chunk['text']}")
