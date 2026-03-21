import streamlit as st

if not st.session_state.get("authenticated", False):
    st.warning("Login first")
    st.stop()

st.title("📚 Documents")

results = st.session_state.get("parsing_results", {})

for file_id, data in results.items():
    st.subheader(data["filename"])
    st.write(f"Scanned: {data['is_scanned']}")
    st.write(f"Path: {data['path']}")

st.divider()

st.subheader("Chunks")

chunks = st.session_state["vector_store"]["chunks"]

for i, chunk in enumerate(chunks[:30]):
    st.write(f"{i+1}. {chunk['text'][:150]}...")
