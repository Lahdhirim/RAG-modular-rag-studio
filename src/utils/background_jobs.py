import threading
from dataclasses import dataclass, field
from enum import Enum


class Status(str, Enum):
    PENDING = "Pending"
    RUNNING = "Running"
    DONE = "Done"
    ERROR = "Error"


@dataclass
class FileJob:
    file_id: str
    filename: str
    status: Status = Status.PENDING
    progress_msg: str = "Not started"
    error: str = ""


@dataclass
class ProcessingJob:
    job_id: str
    files: list[FileJob]
    status: Status = Status.PENDING
    error: str = ""
    parsing_results: dict = field(default_factory=dict)
    chunks: list = field(default_factory=list)
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    def update_file(
        self,
        file_id: str,
        status: Status,
        msg: str = "",
        error: str = "",
    ) -> None:
        with self._lock:
            for file_job in self.files:
                if file_job.file_id == file_id:
                    file_job.status = status
                    file_job.progress_msg = msg
                    file_job.error = error
                    break

    def set_status(self, status: Status) -> None:
        with self._lock:
            self.status = status

    def set_error(self, error: str) -> None:
        with self._lock:
            self.status = Status.ERROR
            self.error = error

    def add_result(self, file_id: str, result: dict, chunks: list[dict]) -> None:
        with self._lock:
            self.parsing_results[file_id] = result
            self.chunks.extend(chunks)
