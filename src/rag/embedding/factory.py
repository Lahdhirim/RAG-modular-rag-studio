from src.config_loader import EmbeddingMethodConfig
from src.rag.embedding.registry import EMBEDDING_REGISTRY
from src.utils.logger_config import logger


def init_embedding(
    embedding_name: str,
    embedding_config: EmbeddingMethodConfig,
):

    embedding_instance = EMBEDDING_REGISTRY.get(embedding_name)

    if not embedding_instance:

        raise ValueError(f"Unsupported embedding: " f"{embedding_name}")

    logger.info(f"Selected embedding: {embedding_name} | Config: {embedding_config}")

    return embedding_instance(params=embedding_config.params)
