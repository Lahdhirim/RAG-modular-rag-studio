from typing import Optional

from src.config_loader import LLMProviderConfig
from src.rag.llms.registry import LLM__REGISTRY
from src.utils.logger_config import logger


def init_chat_llm(
    llm_provider_name: str,
    llm_provider_config: LLMProviderConfig,
    api_key: Optional[str] = None,
):

    llm_instance = LLM__REGISTRY.get(llm_provider_name)

    if not llm_instance:

        raise ValueError(f"Unsupported LLM provider: " f"{llm_provider_name}")

    logger.info(
        f"Selected LLM provider: {llm_provider_name} | Config: {llm_provider_config}"
    )

    return llm_instance(config=llm_provider_config, api_key=api_key)
