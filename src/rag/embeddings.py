import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings

from src.utils.logger_config import logger


def load_embeddings_model(model_name: str):
    try:
        return HuggingFaceEmbeddings(model_name=model_name)
    except Exception as e:
        logger.error(f"Error loading embeddings model: {e}")
        raise RuntimeError(f"Failed to load embeddings model: {model_name}") from e


def embed_chunks(chunks, model):

    # TODO: Add Schema (state and chunks)
    texts = [c["text"] for c in chunks]

    vectors = model.embed_documents(texts)

    matrix = np.array(vectors)
    matrix = matrix / np.linalg.norm(matrix, axis=1, keepdims=True)

    return matrix


def embed_query(query, model):
    vec = np.array(model.embed_query(query))
    return vec / np.linalg.norm(vec)
