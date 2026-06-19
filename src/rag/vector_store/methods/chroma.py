import chromadb

from src.rag.vector_store.base_vector_store import BaseVectorStore
from src.utils.logger_config import vector_store_logger
from src.utils.schema import ChunksSchema, RetrievalSchema


class ChromaVectorStore(BaseVectorStore):
    """ChromaDB implementation of vector store."""

    def __init__(self, params: dict | None = None):
        """Initialize ChromaDB vector store.

        Args:
            params: Configuration parameters:
                - persist_dir (str | None): Path for persistent storage.
                - distance_metric (str): One of "cosine", "euclidean", "manhattan"
                  (default: "cosine").
                - collection_name (str): ChromaDB collection name (default: "documents").
        """
        super().__init__(params)

        persist_dir = self.params.get("persist_dir", None)
        self.collection_name = self.params.get("collection_name", "documents")
        self.distance_metric = self.params.get("distance_metric", "cosine")

        # Initialize Chroma client
        if persist_dir:
            self.client = chromadb.PersistentClient(path=persist_dir)
        else:
            self.client = chromadb.EphemeralClient()

        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": self.distance_metric},
        )

    def store(
        self,
        ids: list[str],
        embeddings: list[list[float]],
        chunks: list[str],
        metadata: list[dict] | None = None,
    ) -> None:
        """Store embeddings and chunks in ChromaDB."""
        if metadata is None:
            metadata = [{} for _ in ids]

        self.collection.upsert(
            ids=ids,
            embeddings=embeddings,
            documents=chunks,
            metadatas=metadata,
        )

    def search(self, query_embedding: list[float], top_k: int = 5) -> list[dict]:
        """Search for similar chunks using query embedding.

        Returns:
            List of dictionaries with keys: 'id', 'text', 'score', 'metadata'.
        """
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )

        output = []
        if results["ids"] and len(results["ids"]) > 0:
            for i, doc_id in enumerate(results["ids"][0]):
                output.append(
                    {
                        RetrievalSchema.ID: doc_id,
                        RetrievalSchema.TEXT: results["documents"][0][i],
                        RetrievalSchema.SCORE: 1 - results["distances"][0][i],
                        RetrievalSchema.METADATA: (
                            results["metadatas"][0][i] if results["metadatas"] else {}
                        ),
                    }
                )

        return output

    def delete(self, ids: list[str]) -> None:
        """Delete chunks by IDs from ChromaDB."""
        self.collection.delete(ids=ids)
        vector_store_logger.warning(f"Deleted {len(ids)} chunks with IDs: {ids}")

    def clear(self) -> None:
        """Clear all chunks from ChromaDB collection."""
        # Get all IDs and delete them
        all_results = self.collection.get()
        if all_results["ids"]:
            all_results_ids = all_results["ids"]
            self.delete(ids=all_results_ids)
            vector_store_logger.warning(
                f"Deleted {len(all_results_ids)} chunks with IDs: {all_results_ids}"
            )

    def get(
        self,
        ids: list[str] | None = None,
        include: list[str] | None = None,
    ) -> dict:
        if include is None:
            include = ["documents", "metadatas"]

        kwargs = {"include": include}

        if ids is not None:
            kwargs["ids"] = ids

        return self.collection.get(**kwargs)

    def get_source_ids(self) -> set[str]:
        results = self.collection.get(include=["metadatas"])

        return {
            metadata[ChunksSchema.SOURCE_ID]
            for metadata in results["metadatas"]
            if metadata and ChunksSchema.SOURCE_ID in metadata
        }

    def count(self) -> int:
        """Return the number of documents in the ChromaDB collection."""
        return self.collection.count()
