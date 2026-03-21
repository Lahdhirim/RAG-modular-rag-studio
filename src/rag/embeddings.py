import numpy as np
from langchain_huggingface import HuggingFaceEmbeddings


def load_embeddings_model():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


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
