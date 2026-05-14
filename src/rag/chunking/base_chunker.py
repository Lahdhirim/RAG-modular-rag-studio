from abc import ABC, abstractmethod


class BaseChunker(ABC):

    def __init__(self, params: dict | None = None):

        self.params = params or {}

    @abstractmethod
    def chunk(self, text: str):
        pass
