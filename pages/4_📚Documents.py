import streamlit as st

from src.utils.schema import ChunksSchema, SessionStateSchema

# Set Streamlit page configuration
st.set_page_config(page_title="Documents", layout="wide")
st.title("📚 Documents")

if not st.session_state.get(SessionStateSchema.AUTHENTICATED, False):
    st.warning("You need to log in first to access this page.")
    st.stop()

vector_store = st.session_state[SessionStateSchema.VECTOR_STORE]
if vector_store.count() == 0:
    st.warning("Upload documents first")
    st.stop()

results = vector_store.get(include=["documents", "metadatas"])
documents = results["documents"]
metadatas = results["metadatas"]

st.subheader("Chunks")
for i, (doc, metadata) in enumerate(
    zip(documents, metadatas),
    start=1,
):
    st.markdown(f"### Chunk {i}")
    st.write(f"Source: {metadata.get(ChunksSchema.SOURCE, 'Unknown')}")
    st.write(f"Scanned: {metadata.get(ChunksSchema.IS_SCANNED, 'Unknown')}")
    st.write(doc[:300] + "...")
    st.divider()
