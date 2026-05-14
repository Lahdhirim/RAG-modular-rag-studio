from src.rag.chunking.methods.recursive import RecursiveChunker
from src.utils.schema import ConfigSchema

CHUNKER_REGISTRY = {
    ConfigSchema.RECURSIVE_CHARACTER: RecursiveChunker,
}
