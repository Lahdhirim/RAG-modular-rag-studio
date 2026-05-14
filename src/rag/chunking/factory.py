from src.config_loader import ChunkingMethodConfig
from src.rag.chunking.registry import CHUNKER_REGISTRY
from src.utils.logger_config import logger


def init_chunker(
    chunker_name: str,
    chunker_config: ChunkingMethodConfig,
):

    chunker_instance = CHUNKER_REGISTRY.get(chunker_name)

    if not chunker_instance:

        raise ValueError(f"Unsupported chunker: " f"{chunker_name}")

    logger.info(f"Selected chunker: {chunker_name} | Config: {chunker_config}")

    return chunker_instance(params=chunker_config.params)
