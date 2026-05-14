class ConfigSchema:
    DOCLING = "docling"
    RECURSIVE_CHARACTER = "recursive_character"
    HUGGING_FACE = "hugging_face"


class SessionStateSchema:
    INITIALIZED = "initialized"
    AUTHENTICATED = "authenticated"
    CONFIG = "config"
    PIPELINE_CONFIG = "pipeline_config"
    PARSER_NAME = "parser_name"
    PARSER_CONFIG = "parser_config"
    CHUNKER_NAME = "chunker_name"
    CHUNKER_CONFIG = "chunker_config"
    EMBEDDING_NAME = "embedding_name"
    EMBEDDING_CONFIG = "embedding_config"
    RETRIEVAL_CONFIG = "retrieval_config"
    KEYS = "keys"
    COPIED_DIR = "copied_dir"
    OUTPUT_DIR = "output_dir"
    PARSING_RESULTS = "parsing_results"
    CURRENT_JOB = "current_job"
    VECTOR_STORE = "vector_store"
    NATIVE_PARSER = "native_parser"
    OCR_PARSER = "ocr_parser"
    PARSERS_LOGGED = "parsers_logged"
    EMBEDDINGS_LOGGED = "embeddings_logged"
    EMBEDDER = "embedder"
    SCANNED_MAP = "scanned_map"
    CHUNKER_LOGGED = "chunker_logged"
    CHUNKER_METHOD = "chunker_method"


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
