from src.rag.llms.providers.openai_compatible import OpenAICompatibleLLM
from src.utils.schema import ConfigSchema

LLM__REGISTRY = {
    ConfigSchema.OPENAI: OpenAICompatibleLLM,
}
