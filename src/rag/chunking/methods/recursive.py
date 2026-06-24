from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.rag.chunking.base_chunker import BaseChunker
from src.utils.logger_config import logger


class RecursiveChunker(BaseChunker):

    def __init__(self, params=None):

        super().__init__(params)

        chunk_size = self.params.get(
            "chunk_size",
            500,
        )
        chunk_overlap = self.params.get(
            "chunk_overlap",
            50,
        )
        separators = self.params.get("separators", ["\n\n", " ", ""])
        logger.info(
            f"Initialized RecursiveCharacterTextSplitter with chunk_size={chunk_size} | chunk_overlap={chunk_overlap} | separators={separators}"
        )

        self.chunker = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=separators,
        )

    def chunk(self, text: str):

        return self.chunker.split_text(text)
