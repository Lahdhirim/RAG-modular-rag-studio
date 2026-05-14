from src.rag.embedding.methods.huggingface import HuggingFaceEmbedding
from src.utils.schema import ConfigSchema

EMBEDDING_REGISTRY = {
    ConfigSchema.HUGGING_FACE: HuggingFaceEmbedding,
}
