from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from src.config_loader import LLMProviderConfig


@dataclass
class LLMResponse:
    success: bool
    message: str
    status_code: int
    error: str | None = None


class BaseLLM(ABC):

    def __init__(self, config: LLMProviderConfig, api_key: Optional[str] = None):

        self.config = config
        self.api_key = api_key
        self.chat_history = [{"role": "system", "content": self.config.system_prompt}]
        self.is_available = False

    @abstractmethod
    def initialize_client(self):
        pass

    @abstractmethod
    def generate(self, message: str) -> LLMResponse:
        pass

    def get_config(self):
        return self.config

    # TODO: Add a method to reset the chat history

    @abstractmethod
    def _ping(self) -> bool:
        pass
