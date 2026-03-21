import streamlit as st

# Set Streamlit page configuration
st.set_page_config(page_title="Documents", layout="wide")
st.title("📚 Documents")

if not st.session_state.get("authenticated", False):
    st.warning("You need to log in first to access this page.")
    st.stop()

results = st.session_state.get("parsing_results", {})

if not results:
    st.warning("Upload documents first")
    st.stop()

for file_id, data in results.items():
    st.subheader(data["metadata"]["filename"])
    st.write(f"Scanned: {data['metadata']['is_scanned']}")

st.divider()

st.subheader("Chunks")

chunks = st.session_state["vector_store"]["chunks"]

for i, chunk in enumerate(chunks[:30]):
    st.write(f"{i+1}. {chunk['text'][:150]}...")
