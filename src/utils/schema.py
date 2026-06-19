class ConfigSchema:
    DOCLING = "docling"
    RECURSIVE_CHARACTER = "recursive_character"
    HUGGING_FACE = "hugging_face"
    OPENAI = "openai"
    CHROMA = "chroma"


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
    COPIED_DIR = "copied_dir"
    OUTPUT_DIR = "output_dir"
    PARSING_RESULTS = "parsing_results"
    CURRENT_JOB = "current_job"
    VECTOR_STORE = "vector_store"
    NATIVE_PARSER = "native_parser"
    OCR_PARSER = "ocr_parser"
    PARSERS_LOGGED = "parsers_logged"
    EMBEDDER = "embedder"
    EMBEDDINGS_LOGGED = "embeddings_logged"
    SCANNED_MAP = "scanned_map"
    CHUNKER_METHOD = "chunker_method"
    CHUNKER_LOGGED = "chunker_logged"
    LLM_PROVIDER_NAME = "llm_provider_name"
    LLM_PROVIDER_CONFIG = "llm_provider_config"
    CHAT_LLM = "chat_llm"
    LLM_LOGGED = "llm_logged"
    MESSAGES = "messages"
    VECTOR_STORE_NAME = "vector_store_name"
    VECTOR_STORE_CONFIG = "vector_store_config"
    VECTOR_STORE_LOGGED = "vector_store_logged"


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


class RetrievalSchema:
    ID = "id"
    TEXT = "text"
    SCORE = "score"
    METADATA = "metadata"
