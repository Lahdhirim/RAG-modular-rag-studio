import streamlit as st

from src.utils.logger_config import chat_logger, logger
from src.utils.schema import ChunksSchema, RetrievalSchema, SessionStateSchema

# Set Streamlit page configuration
st.set_page_config(page_title="Chat", layout="wide")
st.title("💬 Chat")

if not st.session_state.get(SessionStateSchema.AUTHENTICATED, False):
    st.warning("You need to log in first to access this page.")
    st.stop()

vector_store = st.session_state[SessionStateSchema.VECTOR_STORE]
if vector_store.count() == 0:
    st.warning("Upload documents first")
    st.stop()

embedder = st.session_state[SessionStateSchema.EMBEDDER]

# Initialize chat history for UI
if SessionStateSchema.MESSAGES not in st.session_state:
    st.session_state[SessionStateSchema.MESSAGES] = []

# Display previous chat messages
for message in st.session_state[SessionStateSchema.MESSAGES]:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if vector_store.count() != 0:
    chat_llm = st.session_state[SessionStateSchema.CHAT_LLM]

    query = st.chat_input("Ask your question here...")
    if query:

        # Display user message
        st.session_state[SessionStateSchema.MESSAGES].append(
            {
                "role": "user",
                "content": query,
            }
        )
        with st.chat_message("user"):
            st.markdown(query)
        logger.info(f"Received query: {query}")

        # Embed the query
        query_embedding = embedder.embed_query(query=query)

        # Compute cosine similarity
        # Get top k most relevant chunks and filter by similarity threshold
        top_k = st.session_state[SessionStateSchema.PIPELINE_CONFIG][
            SessionStateSchema.RETRIEVAL_CONFIG
        ].top_k
        similarity_threshold = st.session_state[SessionStateSchema.PIPELINE_CONFIG][
            SessionStateSchema.RETRIEVAL_CONFIG
        ].similarity_threshold
        results = vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
        )
        logger.info(
            f"Retrieved {len(results)} chunks from vector store for query: {query}"
        )
        filtered_chunks = [
            result
            for result in results
            if result[RetrievalSchema.SCORE] >= similarity_threshold
        ]
        logger.info(f"Top chunks: {filtered_chunks}")

        # Display results
        if chat_llm and chat_llm.is_available:
            context = "\n\n".join(
                chunk[RetrievalSchema.TEXT] for chunk in filtered_chunks
            )
            augmented_query = f"""
                Use the following context to answer the question.

                Context:
                {context}

                Question:
                {query}
                """

            chat_logger.info(f"Augmented query sent to the LLM: {augmented_query}")
            response = chat_llm.generate(message=augmented_query)
            if response.success:
                with st.chat_message("assistant"):
                    st.markdown(response.message)

                    # Display top relevant chunks for transparency
                    with st.expander("📚 References"):

                        for i, chunk in enumerate(filtered_chunks, start=1):
                            st.markdown(f"### Chunk {i}")
                            st.markdown(
                                f"**Source:** {chunk[RetrievalSchema.METADATA].get(ChunksSchema.SOURCE, 'Unknown')}"
                            )
                            st.markdown(chunk[RetrievalSchema.TEXT])
                            st.caption(f"Score: {chunk[RetrievalSchema.SCORE]:.4f}")
                            st.divider()

                st.session_state[SessionStateSchema.MESSAGES].append(
                    {
                        "role": "assistant",
                        "content": response.message,
                    }
                )
                chat_logger.info(f"LLM response: {response.message}")

            else:
                with st.chat_message("assistant"):

                    st.error(f"LLM generation failed: {response.error}")

                    st.write("### Top relevant chunks:")

                    for chunk in filtered_chunks:
                        st.write(f"- {chunk[RetrievalSchema.TEXT]}")
                chat_logger.error(f"LLM generation error: {response.error}")
                chat_logger.info(f"Top relevant chunk: {chunk[RetrievalSchema.TEXT]}")

        else:
            with st.chat_message("assistant"):

                st.error(
                    "LLM Chat is not available. Only raw retrieval results are displayed."
                )

                st.write("### Top relevant chunks:")

                for chunk in filtered_chunks:
                    st.write(f"- {chunk[RetrievalSchema.TEXT]}")
                    chat_logger.info(
                        f"Top relevant chunk: {chunk[RetrievalSchema.TEXT]}"
                    )
