from langchain_huggingface import HuggingFaceEmbeddings

from src.rag.embedding.base_embedder import BaseEmbedding
from src.utils.logger_config import logger


class HuggingFaceEmbedding(BaseEmbedding):

    def __init__(self, params=None):

        super().__init__(params)

        model_name = self.params.get(
            "embedding_model",
            "sentence-transformers/all-MiniLM-L6-v2",
        )

        try:

            self.model = HuggingFaceEmbeddings(model_name=model_name)

            logger.info(f"Loaded embedding model: " f"{model_name}")

        except Exception as e:

            logger.error(f"Error loading embedding model: {e}")

            raise RuntimeError(
                f"Failed to load embedding model: " f"{model_name}"
            ) from e

    def embed_documents(
        self,
        texts: list[str],
    ):

        return self.model.embed_documents(texts)

    def embed_query(
        self,
        text: str,
    ):

        return self.model.embed_query(text)
