from src.rag.vector_store.methods.chroma import ChromaVectorStore
from src.utils.schema import ConfigSchema

VECTOR_STORE_REGISTRY = {
    ConfigSchema.CHROMA: ChromaVectorStore,
}
