import numpy as np

from src.rag.embedding.base_embedder import BaseEmbedding
from src.utils.schema import ChunksSchema


def embed_chunks(chunks, embedder: BaseEmbedding):

    texts = [c[ChunksSchema.TEXT] for c in chunks]

    vectors = embedder.embed_documents(texts)

    matrix = np.array(vectors)
    matrix = matrix / np.linalg.norm(matrix, axis=1, keepdims=True)

    return matrix


def embed_query(query, embedder: BaseEmbedding):

    vec = np.array(embedder.embed_query(query))

    return vec / np.linalg.norm(vec)
