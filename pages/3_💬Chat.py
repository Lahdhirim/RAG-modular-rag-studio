import numpy as np
import streamlit as st

from src.rag.embedding.utils import embed_chunks, embed_query
from src.utils.logger_config import logger
from src.utils.schema import ChunksSchema, SessionStateSchema

# Set Streamlit page configuration
st.set_page_config(page_title="Chat", layout="wide")
st.title("💬 Chat")

if not st.session_state.get(SessionStateSchema.AUTHENTICATED, False):
    st.warning("You need to log in first to access this page.")
    st.stop()

all_chunks = st.session_state[SessionStateSchema.VECTOR_STORE]["chunks"]
if not all_chunks:
    st.warning("Upload documents first")
    st.stop()

embedder = st.session_state[SessionStateSchema.EMBEDDER]

# Embeddings
if st.session_state[SessionStateSchema.VECTOR_STORE]["matrix"] is None:
    matrix = embed_chunks(chunks=all_chunks, embedder=embedder)
    st.session_state[SessionStateSchema.VECTOR_STORE]["matrix"] = matrix
    logger.info("Computed embeddings for all chunks and stored in session state.")

if st.session_state[SessionStateSchema.VECTOR_STORE]["matrix"] is not None:
    matrix = st.session_state[SessionStateSchema.VECTOR_STORE]["matrix"]

    query = st.text_input("Ask your question here:")
    if query:
        logger.info(f"Received query: {query}")
        query_vec = embed_query(query=query, embedder=embedder)

        # Compute cosine similarity
        similarities = matrix @ query_vec

        # Get top k most relevant chunks and filter by similarity threshold
        # TODO: Initialize retrieval component and get its configuration
        best_indexes = np.argsort(similarities)[-5:]
        filtered_indexes = [
            best_index for best_index in best_indexes if similarities[best_index] > 0.5
        ]
        logger.info(
            f"Best matching chunk indexes: {best_indexes} with respective similarities: {similarities[best_indexes]}, filtered indexes: {filtered_indexes}"
        )

        top_chunks = [all_chunks[i] for i in filtered_indexes]
        logger.info(f"Top chunks: {top_chunks}")

        # Display results
        st.write("### Top relevant chunks:")
        for chunk in top_chunks:
            st.write(f"- {chunk[ChunksSchema.TEXT]}")
