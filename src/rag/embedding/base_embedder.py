from abc import ABC, abstractmethod


class BaseEmbedding(ABC):

    def __init__(self, params: dict | None = None):

        self.params = params or {}

    @abstractmethod
    def embed_documents(
        self,
        texts: list[str],
    ):
        pass

    @abstractmethod
    def embed_query(
        self,
        query: str,
    ):
        pass
