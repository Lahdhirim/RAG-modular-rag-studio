import shutil
import tempfile
from pathlib import Path

import streamlit as st

from src.rag.processing import chunk_text, generate_file_id, pdf_to_text
from src.utils.logger_config import logger

if not st.session_state.get("authenticated", False):
    st.warning("Login first")
    st.stop()

st.title("📤 Upload PDFs")

uploaded_files = st.file_uploader("Upload PDF", type="pdf", accept_multiple_files=True)

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

                converter = (
                    st.session_state["ocr_converter"]
                    if is_scanned
                    else st.session_state["native_converter"]
                )

                if not is_scanned:
                    # Native PDF
                    with st.spinner(f"Extracting text from {uploaded_file.name}..."):
                        text = pdf_to_text(pdf_path=str(temp_path), converter=converter)
                        logger.info(
                            f"Text extraction completed for {uploaded_file.name}"
                        )
                else:
                    # OCR
                    with st.spinner(f"OCR on {uploaded_file.name}..."):
                        text = pdf_to_text(pdf_path=str(temp_path), converter=converter)
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
                st.session_state["vector_store"]["chunks"].extend(chunks_with_metadata)

                # Update session state with parsing results
                st.session_state["parsing_results"][file_id] = {
                    "filename": filename,
                    "text": text,
                    "path": str(output_path),
                    "is_scanned": is_scanned,
                }

        st.success("All done! You can now ask questions about your documents.")
        logger.info("All files processed successfully.")
