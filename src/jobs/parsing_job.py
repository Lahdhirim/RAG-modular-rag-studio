import shutil
import tempfile
from pathlib import Path

from src.utils.background_jobs import ProcessingJob, Status
from src.utils.logger_config import processing_job_logger as logger
from src.utils.schema import (
    ChunksSchema,
    DocumentsSchema,
    InputFileSchema,
    SessionStateSchema,
)


def save_chunks(
    chunks: list[dict],
    output_path: Path,
) -> None:
    """Save chunks and metadata as a Markdown file."""

    content = []

    for i, chunk in enumerate(chunks, start=1):
        content.append(f"""# Chunk {i}

**Source:** {chunk[ChunksSchema.SOURCE]}
**Source ID:** {chunk[ChunksSchema.SOURCE_ID]}
**Scanned:** {chunk[ChunksSchema.IS_SCANNED]}

{chunk[ChunksSchema.TEXT]}

---
""")

    output_path.write_text(
        "\n".join(content),
        encoding="utf-8",
    )


def run_parsing_job(job: ProcessingJob, files_data: dict, session_refs: dict):

    logger.info(f"Starting processing job {job.job_id} with {len(files_data)} files")
    job.set_status(Status.RUNNING)

    successfully_processed_files, failed_files = 0, 0

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            for file_data in files_data:
                file_id = file_data[InputFileSchema.FILE_ID]
                filename = file_data[InputFileSchema.FILENAME]
                file_bytes = file_data[InputFileSchema.BYTES]
                is_scanned = file_data[InputFileSchema.SCANNED]

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
                    copied_path = session_refs[SessionStateSchema.COPIED_DIR] / filename
                    shutil.copy(temp_path, copied_path)
                    logger.info(f"Copied {filename} to {copied_path}")

                    # Select parser based on scanned/native status
                    parser = (
                        session_refs[SessionStateSchema.OCR_PARSER]
                        if is_scanned
                        else session_refs[SessionStateSchema.NATIVE_PARSER]
                    )

                    # Convert Document to text
                    msg = "🔍 OCR..." if is_scanned else "🔍 Extracting..."
                    job.update_file(file_id=file_id, status=Status.RUNNING, msg=msg)
                    text, successfully_processed_pages, failed_pages = parser.parse(
                        pdf_path=str(temp_path)
                    )

                    if successfully_processed_pages > 0:
                        logger.info(
                            f"Successfully parsed {successfully_processed_pages} pages for {filename}"
                        )

                        # Save in Markdown format
                        stem = Path(filename).stem
                        output_path = (
                            session_refs[SessionStateSchema.OUTPUT_DIR] / f"{stem}.md"
                        )
                        output_path.write_text(text, encoding="utf-8")
                        logger.info(f"Saved Markdown file: {output_path}")

                        # Chunking
                        job.update_file(
                            file_id=file_id,
                            status=Status.RUNNING,
                            msg="📦 Chunking...",
                        )
                        chunker_method = session_refs[SessionStateSchema.CHUNKER_METHOD]
                        job.update_file(
                            file_id=file_id, status=Status.RUNNING, msg="📦 Chunking..."
                        )
                        chunks = chunker_method.chunk(text=text)

                        logger.info(
                            f"Chunked text into {len(chunks)} chunks for {filename}"
                        )
                        chunks_with_metadata = [
                            {
                                ChunksSchema.TEXT: chunk,
                                ChunksSchema.SOURCE: stem,
                                ChunksSchema.SOURCE_ID: file_id,
                                ChunksSchema.IS_SCANNED: is_scanned,
                            }
                            for chunk in chunks
                        ]

                        # Save chunks to chunking output directory
                        chunking_output_path = (
                            session_refs[SessionStateSchema.CHUNKING_OUTPUT_DIR]
                            / f"{stem}_chunks.md"
                        )
                        save_chunks(chunks_with_metadata, chunking_output_path)
                        logger.info(f"Saved chunks file: {chunking_output_path}")

                        # Update job with results
                        job.add_result(
                            file_id=file_id,
                            result={
                                DocumentsSchema.TEXT: text,
                                DocumentsSchema.METADATA: {
                                    DocumentsSchema.FILENAME: filename,
                                    DocumentsSchema.IS_SCANNED: is_scanned,
                                },
                            },
                            chunks=chunks_with_metadata,
                        )

                        if failed_pages == 0:
                            # Update file status to done
                            job.update_file(
                                file_id=file_id, status=Status.DONE, msg="✅ Done"
                            )

                        else:
                            logger.warning(
                                f"Some pages failed to parse for {filename}: {failed_pages} pages failed"
                            )
                            job.update_file(
                                file_id=file_id,
                                status=Status.DONE,
                                msg=f"✅ Done with warnings: {failed_pages} pages failed",
                                error=f"⚠️ Warning: {failed_pages} pages could not be parsed",
                            )

                        successfully_processed_files += 1

                    else:
                        logger.warning(
                            f"No pages were successfully parsed for {filename}"
                        )
                        job.update_file(
                            file_id=file_id,
                            status=Status.ERROR,
                            error=f"❌ No pages could be parsed for {filename}",
                        )
                        failed_files += 1

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
