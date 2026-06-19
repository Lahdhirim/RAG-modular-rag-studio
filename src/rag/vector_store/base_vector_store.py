from abc import ABC, abstractmethod


class BaseVectorStore(ABC):
    """Abstract base class for vector store implementations."""

    def __init__(self, params: dict | None = None):
        """Initialize vector store with configuration parameters.

        Args:
            params: Configuration parameters specific to the vector store implementation.
        """
        self.params = params or {}

    @abstractmethod
    def store(
        self,
        ids: list[str],
        embeddings: list[list[float]],
        documents: list[str],
        metadata: list[dict] | None = None,
    ) -> None:
        """Store embeddings and documents in vector store.

        Args:
            ids: List of unique document identifiers.
            embeddings: List of embedding vectors.
            documents: List of document texts.
            metadata: Optional list of metadata dictionaries for each document.
        """
        pass

    @abstractmethod
    def search(self, query_embedding: list[float], top_k: int = 5) -> list[dict]:
        """Search for similar documents.

        Args:
            query_embedding: Query embedding vector.
            top_k: Number of top results to return.

        Returns:
            List of dictionaries with keys: 'id', 'document', 'distance', 'metadata'.
        """
        pass

    @abstractmethod
    def delete(self, ids: list[str]) -> None:
        """Delete documents by IDs.

        Args:
            ids: List of document IDs to delete.
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """Clear all documents from vector store."""
        pass

    @abstractmethod
    def get(
        self,
        ids: list[str] | None = None,
        include: list[str] | None = None,
    ) -> dict:
        """Retrieve documents from the vector store."""
        pass

    @abstractmethod
    def count(self) -> int:
        """Return the number of documents in the vector store."""
        pass
