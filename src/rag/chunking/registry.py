from src.rag.chunking.methods.recursive import RecursiveChunker

CHUNKER_REGISTRY = {
    "recursive_character": RecursiveChunker,
}
