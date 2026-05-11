import threading
import time
import uuid

import streamlit as st

from src.rag.processing import generate_file_id
from src.services.processing_job import run_processing_job
from src.utils.background_jobs import FileJob, ProcessingJob, Status
from src.utils.logger_config import logger
from src.utils.schema import InputFileSchema, SessionStateSchema

if not st.session_state.get(SessionStateSchema.AUTHENTICATED, False):
    st.warning("You need to log in first to access this page.")
    st.stop()

st.title("📤 Upload PDFs")

# Get current job status
job = st.session_state.get(SessionStateSchema.CURRENT_JOB, None)
is_processing = job is not None and job.status == Status.RUNNING
uploaded_files = st.file_uploader(
    "Upload PDF", type="pdf", accept_multiple_files=True, disabled=is_processing
)
if SessionStateSchema.PARSING_RESULTS not in st.session_state:
    st.session_state[SessionStateSchema.PARSING_RESULTS] = {}

# Initialize scanned file map
if SessionStateSchema.SCANNED_MAP not in st.session_state:
    st.session_state[SessionStateSchema.SCANNED_MAP] = {}
scanned_map = st.session_state[SessionStateSchema.SCANNED_MAP]

# Upload and process PDFs
if uploaded_files:

    # TODO: This is a temporary fix, scanned file detection will be implemented in the future
    # Scanned PDF checkboxes
    for uploaded_file in uploaded_files:
        scanned_map[uploaded_file.name] = st.checkbox(
            f"Is {uploaded_file.name} a scanned PDF?", key=uploaded_file.name
        )

    if st.button("Process PDF files", disabled=is_processing):

        files_data = []
        job = ProcessingJob(job_id=str(uuid.uuid4()), files=[])

        for uploaded_file in uploaded_files:
            file_id = generate_file_id(uploaded_file)

            if file_id in st.session_state[SessionStateSchema.PARSING_RESULTS]:
                continue

            files_data.append(
                {
                    InputFileSchema.FILE_ID: file_id,
                    InputFileSchema.FILENAME: uploaded_file.name,
                    InputFileSchema.BYTES: uploaded_file.getbuffer().tobytes(),
                    InputFileSchema.SCANNED: scanned_map[uploaded_file.name],
                }
            )

            job.files.append(FileJob(file_id=file_id, filename=uploaded_file.name))

        # Run processing in a separate thread
        if files_data:
            session_refs = {
                SessionStateSchema.COPIED_DIR: st.session_state[
                    SessionStateSchema.COPIED_DIR
                ],
                SessionStateSchema.OUTPUT_DIR: st.session_state[
                    SessionStateSchema.OUTPUT_DIR
                ],
                SessionStateSchema.OCR_CONVERTER: st.session_state[
                    SessionStateSchema.OCR_CONVERTER
                ],
                SessionStateSchema.NATIVE_CONVERTER: st.session_state[
                    SessionStateSchema.NATIVE_CONVERTER
                ],
                SessionStateSchema.CHUNKER_METHOD: st.session_state[
                    SessionStateSchema.CHUNKER_METHOD
                ],
            }

            logger.info(
                f"Initiating processing job {job.job_id} for {len(files_data)} files"
            )
            thread = threading.Thread(
                target=run_processing_job,
                args=(job, files_data, session_refs),
                daemon=True,
            )

            st.session_state[SessionStateSchema.CURRENT_JOB] = job
            logger.info(f"Starting background thread for job {job.job_id}")
            thread.start()

# Display job status
if job is not None:

    st.subheader("Job Status Process")

    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
    col1.markdown("**File**")
    col2.markdown("**Scanned**")
    col3.markdown("**Status**")
    col4.markdown("**Progress**")
    col5.markdown("**Error**")
    for f in job.files:
        col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
        col1.write(f"**{f.filename}**")
        col2.write(f"{scanned_map.get(f.filename, 'Unknown')}")
        col3.write(f"Status: {f.status.value}")
        col4.write(f"{f.progress_msg}")
        if f.error:
            col5.error(f"Error: {f.error}")

    if job.status == Status.DONE:
        st.success("✅ Done!")
        logger.info(
            f"Processing job {job.job_id} completed successfully with {len(job.files)} files processed."
        )

        # Inject results
        st.session_state[SessionStateSchema.PARSING_RESULTS].update(job.parsing_results)
        st.session_state[SessionStateSchema.VECTOR_STORE]["chunks"].extend(job.chunks)
        logger.info(
            f"Updated session state with parsing results and chunks from job {job.job_id}. Total chunks in vector store: {len(st.session_state[SessionStateSchema.VECTOR_STORE]['chunks'])}"
        )

        # Clear current job from session state
        st.session_state[SessionStateSchema.CURRENT_JOB] = None

        # Clear scanned map for next uploads
        st.session_state[SessionStateSchema.SCANNED_MAP] = {}

    elif job.status == Status.ERROR:
        st.error(f"Error during processing: {job.error}")
        logger.error(f"Processing job {job.job_id} encountered an error: {job.error}")

    else:
        # Job is still running, refresh every 2 seconds
        time.sleep(2)
        st.rerun()
