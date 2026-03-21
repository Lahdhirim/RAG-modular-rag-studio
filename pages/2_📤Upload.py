import threading
import time
import uuid

import streamlit as st

from src.rag.processing import generate_file_id
from src.services.pocessing_job import run_processing_job
from src.utils.background_jobs import FileJob, ProcessingJob, Status
from src.utils.logger_config import logger

if not st.session_state.get("authenticated", False):
    st.warning("You need to log in first to access this page.")
    st.stop()

st.title("📤 Upload PDFs")

# Get current job status
job = st.session_state.get("current_job")
is_processing = job is not None and job.status == Status.RUNNING
uploaded_files = st.file_uploader(
    "Upload PDF", type="pdf", accept_multiple_files=True, disabled=is_processing
)
if "parsing_results" not in st.session_state:
    st.session_state["parsing_results"] = {}

# Upload and process PDFs
if uploaded_files:

    # TODO: This is a temporary fix, scanned file detection will be implemented in the future
    # Scanned PDF checkboxes
    scanned_map = {}
    for uploaded_file in uploaded_files:
        scanned_map[uploaded_file.name] = st.checkbox(
            f"Is {uploaded_file.name} a scanned PDF?", key=uploaded_file.name
        )

    if st.button("Process PDF files"):

        files_data = []
        job = ProcessingJob(job_id=str(uuid.uuid4()), files=[])

        for uploaded_file in uploaded_files:
            file_id = generate_file_id(uploaded_file)

            if file_id in st.session_state["parsing_results"]:
                continue

            files_data.append(
                {
                    "file_id": file_id,
                    "filename": uploaded_file.name,
                    "bytes": uploaded_file.getbuffer().tobytes(),
                    "is_scanned": scanned_map[uploaded_file.name],
                }
            )

            job.files.append(FileJob(file_id=file_id, filename=uploaded_file.name))

        # Run processing in a separate thread
        if files_data:
            session_refs = {
                "COPIED_DIR": st.session_state["COPIED_DIR"],
                "OUTPUT_DIR": st.session_state["OUTPUT_DIR"],
                "ocr_converter": st.session_state["ocr_converter"],
                "native_converter": st.session_state["native_converter"],
            }

            logger.info(
                f"Initiating processing job {job.job_id} for {len(files_data)} files"
            )
            thread = threading.Thread(
                target=run_processing_job,
                args=(job, files_data, session_refs),
                daemon=True,
            )

            st.session_state["current_job"] = job
            logger.info(f"Starting background thread for job {job.job_id}")
            thread.start()

# Display job status
if job is not None:
    st.subheader("Job Status Process")

    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
    col1.markdown("**File**")
    col2.markdown("**Status**")
    col3.markdown("**Progress**")
    col4.markdown("**Scanned**")
    col5.markdown("**Error**")
    for f in job.files:
        col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
        col1.write(f"**{f.filename}**")
        col2.write(f"Status: {f.status.value}")
        col3.write(f"{f.progress_msg}")
        col4.write(f"Scanned: {scanned_map.get(f.filename, 'Unknown')}")
        if f.error:
            col5.error(f"Error: {f.error}")

    if job.status == Status.DONE:
        st.success("✅ Done!")
        logger.info(
            f"Processing job {job.job_id} completed successfully with {len(job.files)} files processed."
        )

        # Inject results
        st.session_state["parsing_results"].update(job.parsing_results)
        st.session_state["vector_store"]["chunks"].extend(job.chunks)
        logger.info(
            f"Updated session state with parsing results and chunks from job {job.job_id}. Total chunks in vector store: {len(st.session_state['vector_store']['chunks'])}"
        )

        # Clear current job from session state
        st.session_state["current_job"] = None

    elif job.status == Status.ERROR:
        st.error(f"Error during processing: {job.error}")
        logger.error(f"Processing job {job.job_id} encountered an error: {job.error}")

    else:
        # Job is still running, refresh every 2 seconds
        time.sleep(2)
        st.rerun()
