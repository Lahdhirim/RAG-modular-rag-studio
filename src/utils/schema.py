class ParsingSchema:
    DOCLING = "docling"


class SessionStateSchema:
    INITIALIZED = "initialized"
    AUTHENTICATED = "authenticated"
    CONFIG = "config"
    KEYS = "keys"
    COPIED_DIR = "copied_dir"
    OUTPUT_DIR = "output_dir"
    PARSING_RESULTS = "parsing_results"
    CURRENT_JOB = "current_job"
    VECTOR_STORE = "vector_store"
    NATIVE_CONVERTER = "native_converter"
    OCR_CONVERTER = "ocr_converter"
    CONVERTERS_LOGGED = "converters_logged"
    EMBEDDINGS_LOGGED = "embeddings_logged"
    EMBEDDING_MODEL = "embedding_model"
    SCANNED_MAP = "scanned_map"


class InputFileSchema:
    FILE_ID = "file_id"
    FILENAME = "filename"
    BYTES = "bytes"
    SCANNED = "is_scanned"


class DocumentsSchema:
    TEXT = "text"
    METADATA = "metadata"
    FILENAME = "filename"
    IS_SCANNED = "is_scanned"


class ChunksSchema:
    TEXT = "text"
    SOURCE = "source"
    SOURCE_ID = "source_id"
    IS_SCANNED = "is_scanned"
