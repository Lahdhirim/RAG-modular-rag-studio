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


# Initialize chat history for UI
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state[SessionStateSchema.VECTOR_STORE]["matrix"] is not None:
    matrix = st.session_state[SessionStateSchema.VECTOR_STORE]["matrix"]
    chat_llm = st.session_state[SessionStateSchema.CHAT_LLM]

    query = st.chat_input("Ask your question here...")
    if query:

        # Display user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": query,
            }
        )
        with st.chat_message("user"):
            st.markdown(query)
        logger.info(f"Received query: {query}")
        query_vec = embed_query(query=query, embedder=embedder)

        # Compute cosine similarity
        similarities = matrix @ query_vec

        # Get top k most relevant chunks and filter by similarity threshold
        top_k = st.session_state[SessionStateSchema.PIPELINE_CONFIG][
            SessionStateSchema.RETRIEVAL_CONFIG
        ].top_k
        similarity_threshold = st.session_state[SessionStateSchema.PIPELINE_CONFIG][
            SessionStateSchema.RETRIEVAL_CONFIG
        ].similarity_threshold
        best_indexes = np.argsort(similarities)[-top_k:]
        filtered_indexes = [
            best_index
            for best_index in best_indexes
            if similarities[best_index] > similarity_threshold
        ]
        logger.info(
            f"Best matching chunk indexes: {best_indexes} with respective similarities: {similarities[best_indexes]}, filtered indexes: {filtered_indexes}"
        )

        top_chunks = [all_chunks[i] for i in filtered_indexes]
        logger.info(f"Top chunks: {top_chunks}")

        # Display results
        if chat_llm:
            context = "\n\n".join(chunk[ChunksSchema.TEXT] for chunk in top_chunks)
            augmented_query = f"""
                Use the following context to answer the question.

                Context:
                {context}

                Question:
                {query}
                """
            # TODO: Add logger for chat history and LLM responses
            logger.info(f"Augmented query sent to the LLM: {augmented_query}")
            response = chat_llm.generate(message=augmented_query)
            if response.success:
                with st.chat_message("assistant"):
                    st.markdown(response.message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response.message,
                    }
                )
                logger.info(f"LLM response: {response.message}")

            else:
                with st.chat_message("assistant"):

                    st.error(f"LLM generation failed: {response.error}")

                    st.write("### Top relevant chunks:")

                    for chunk in top_chunks:
                        st.write(f"- {chunk[ChunksSchema.TEXT]}")
                logger.error(f"LLM generation error: {response.error}")

        else:
            with st.chat_message("assistant"):

                st.error(
                    "LLM Chat is not available. Only raw retrieval results are displayed."
                )

                st.write("### Top relevant chunks:")

                for chunk in top_chunks:
                    st.write(f"- {chunk[ChunksSchema.TEXT]}")
