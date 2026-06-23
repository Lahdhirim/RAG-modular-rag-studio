from collections import defaultdict

import streamlit as st

from src.utils.logger_config import logger
from src.utils.schema import ChunksSchema, SessionStateSchema

# Set Streamlit page configuration
st.set_page_config(page_title="Collection", layout="wide")
st.title("📚 Collection")

if not st.session_state.get(SessionStateSchema.AUTHENTICATED, False):
    st.warning("You need to log in first to access this page.")
    st.stop()

vector_store = st.session_state[SessionStateSchema.VECTOR_STORE]
if vector_store.count() == 0:
    st.warning("Upload documents first")
    st.stop()

if (
    SessionStateSchema.COLLECTION_RESULTS not in st.session_state
    or SessionStateSchema.COLLECTION_DOCUMENTS not in st.session_state
):
    logger.info("Fetching collection results from vector store")
    results = vector_store.get(include=["documents", "metadatas"])
    st.session_state[SessionStateSchema.COLLECTION_RESULTS] = results

    documents_by_source = defaultdict(list)

    for doc, metadata in zip(
        results["documents"],
        results["metadatas"],
    ):
        metadata = metadata or {}
        source_id = metadata.get(
            ChunksSchema.SOURCE_ID,
            "unknown",
        )
        documents_by_source[source_id].append((doc, metadata))

    st.session_state[SessionStateSchema.COLLECTION_DOCUMENTS] = documents_by_source

    logger.info("Fetched collection results from vector store")

documents_by_source = st.session_state[SessionStateSchema.COLLECTION_DOCUMENTS]

st.subheader("Documents")

for source_id, chunks in documents_by_source.items():
    first_metadata = chunks[0][1]

    source = first_metadata.get(ChunksSchema.SOURCE, "Unknown")
    is_scanned = first_metadata.get(ChunksSchema.IS_SCANNED, "Unknown")

    st.markdown(f"### 📄 {source}")
    st.write(f"**Source ID:** `{source_id}`")
    st.write(f"**Scanned:** {is_scanned}")
    st.write(f"**Chunks:** {len(chunks)}")

    col1, col2 = st.columns([5, 1])

    with col1:
        show_chunks = st.toggle(
            "Show chunks",
            key=f"toggle_{source_id}",
        )

    with col2:
        if st.button(
            "🗑️ Delete",
            key=f"delete_{source_id}",
            type="primary",
            help="Delete this document and all its chunks from the current collection.",
        ):
            vector_store.delete_source(source_id)

            # Invalidate cache
            st.session_state.pop(
                SessionStateSchema.COLLECTION_RESULTS,
                None,
            )
            st.session_state.pop(
                SessionStateSchema.COLLECTION_DOCUMENTS,
                None,
            )

            logger.info(f"Deleted document '{source}' " f"(source_id={source_id})")

            st.rerun()

    if show_chunks:
        for i, (doc, _) in enumerate(chunks, start=1):
            st.markdown(f"**Chunk {i}**")
            st.write(doc[:500] + ("..." if len(doc) > 500 else ""))
            st.divider()

    st.divider()
