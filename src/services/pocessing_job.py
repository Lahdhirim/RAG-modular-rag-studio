import shutil
import tempfile
from pathlib import Path

from src.rag.processing import chunk_text, pdf_to_text
from src.utils.background_jobs import ProcessingJob, Status
from src.utils.logger_config import processing_job_logger as logger


def run_processing_job(job: ProcessingJob, files_data: dict, session_refs: dict):

    logger.info(f"Starting processing job {job.job_id} with {len(files_data)} files")
    job.set_status(Status.RUNNING)

    successfully_processed_files, failed_files = 0, 0

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            for file_data in files_data:
                file_id = file_data["file_id"]
                filename = file_data["filename"]
                file_bytes = file_data["bytes"]
                is_scanned = file_data["is_scanned"]

                logger.info(
                    f"Processing file {filename}: {{ID: {file_id}, Scanned: {is_scanned}}}"
                )
                job.update_file(
                    file_id=file_id, status=Status.RUNNING, msg="⏳ Starting file"
                )

                try:
                    temp_path = Path(tmpdir) / filename
                    temp_path.write_bytes(file_bytes)

                    # Copy PDF to copied_pdfs directory
                    copied_path = session_refs["COPIED_DIR"] / filename
                    shutil.copy(temp_path, copied_path)
                    logger.info(f"Copied {filename} to {copied_path}")

                    # Select converter based on scanned/native status
                    converter = (
                        session_refs["ocr_converter"]
                        if is_scanned
                        else session_refs["native_converter"]
                    )

                    # Convert PDF to text
                    msg = "🔍 OCR..." if is_scanned else "🔍 Extracting..."
                    job.update_file(file_id=file_id, status=Status.RUNNING, msg=msg)
                    text = pdf_to_text(str(temp_path), converter)

                    # Save in Markdown format
                    stem = Path(filename).stem
                    job.update_file(
                        file_id=file_id,
                        status=Status.RUNNING,
                        msg="💾 Saving Markdown...",
                    )
                    output_path = session_refs["OUTPUT_DIR"] / f"{stem}.md"
                    output_path.write_text(text, encoding="utf-8")
                    logger.info(f"Saved Markdown file: {output_path}")

                    # Chunking
                    job.update_file(
                        file_id=file_id, status=Status.RUNNING, msg="📦 Chunking..."
                    )
                    chunks = chunk_text(text)
                    logger.info(
                        f"Chunked text into {len(chunks)} chunks for {filename}"
                    )
                    chunks_with_metadata = [
                        {
                            "text": chunk,
                            "source": stem,
                            "source_id": file_id,
                            "is_scanned": is_scanned,
                        }
                        for chunk in chunks
                    ]

                    # Update job with results
                    job.add_result(
                        file_id=file_id,
                        result={
                            "text": text,
                            "metadata": {
                                "filename": filename,
                                "is_scanned": is_scanned,
                            },
                        },
                        chunks=chunks_with_metadata,
                    )

                    # Update file status to done
                    job.update_file(file_id=file_id, status=Status.DONE, msg="✅ Done")

                    successfully_processed_files += 1

                except Exception as e:
                    job.update_file(
                        file_id=file_id,
                        status=Status.ERROR,
                        error=f"❌ Error during processing file {filename}: {str(e)}",
                    )
                    failed_files += 1

        logger.info(
            f"Finished processing job {job.job_id}: {successfully_processed_files} files processed successfully, {failed_files} files failed"
        )
        job.set_status(Status.DONE)

    except Exception as e:
        job.set_error(str(e))
