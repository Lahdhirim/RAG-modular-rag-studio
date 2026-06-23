from src.config_loader import VectorStoreConfig
from src.rag.vector_store.registry import VECTOR_STORE_REGISTRY
from src.utils.logger_config import logger


def init_vector_store(vector_store_name: str, vector_store_config: VectorStoreConfig):
    """Initialize a vector store instance from registry."""
    vector_store_instance = VECTOR_STORE_REGISTRY.get(vector_store_name)
    if not vector_store_instance:
        raise ValueError(f"Unsupported vector store: {vector_store_name}")
    logger.info(
        f"Selected vector store: {vector_store_name} | Config: {vector_store_config}"
    )
    return vector_store_instance(params=vector_store_config.params)
