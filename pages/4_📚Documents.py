import streamlit as st

from src.utils.schema import ChunksSchema, DocumentsSchema, SessionStateSchema

# Set Streamlit page configuration
st.set_page_config(page_title="Documents", layout="wide")
st.title("📚 Documents")

if not st.session_state.get(SessionStateSchema.AUTHENTICATED, False):
    st.warning("You need to log in first to access this page.")
    st.stop()

results = st.session_state.get(SessionStateSchema.PARSING_RESULTS, {})

if not results:
    st.warning("Upload documents first")
    st.stop()

for file_id, data in results.items():
    st.subheader(data[DocumentsSchema.METADATA][DocumentsSchema.FILENAME])
    st.write(f"Scanned: {data[DocumentsSchema.METADATA][DocumentsSchema.IS_SCANNED]}")

st.divider()

st.subheader("Chunks")

# TODO: add divison between documents and chunks, and show which chunks belong to which documents
chunks = st.session_state[SessionStateSchema.VECTOR_STORE]["chunks"]

for i, chunk in enumerate(chunks[:30]):
    st.write(f"{i+1}. {chunk[ChunksSchema.TEXT][:150]}...")
