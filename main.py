import os
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import easyocr
import fitz
import numpy as np
import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_text_splitters import CharacterTextSplitter
from PIL import Image

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

reader = easyocr.Reader(["fr", "en"])


def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        result = reader.readtext(np.array(img), detail=0)
        page_text = " ".join(result)
        text += page_text + "\n"

    return text


def process_page(page):
    pix = page.get_pixmap(dpi=300)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    result = reader.readtext(np.array(img), detail=0)
    return " ".join(result)


def pdf_to_text_parallel(pdf_path, max_workers=4):
    doc = fitz.open(pdf_path)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        texts = list(executor.map(process_page, doc))

    return "\n".join(texts)


def chunk_text(text):
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_text(text)


@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def embed_chunks(chunks):
    embeddings = load_embeddings()
    vectors = embeddings.embed_documents(chunks)

    matrix = np.array(vectors)
    matrix = matrix / np.linalg.norm(matrix, axis=1, keepdims=True)

    return matrix


def embed_query(query):
    embeddings = load_embeddings()
    vec = np.array(embeddings.embed_query(query))
    return vec / np.linalg.norm(vec)


if __name__ == "__main__":

    # Streamlit UI
    st.set_page_config(page_title="Simple RAG", layout="wide")
    st.title("📄 Simple RAG")

    uploaded_file = st.file_uploader("Upload PDF", type="pdf")

    # Chunking & Embedding
    if uploaded_file:
        if st.button("Process PDF"):

            with tempfile.TemporaryDirectory() as tmpdir:
                path = Path(tmpdir) / uploaded_file.name
                path.write_bytes(uploaded_file.getbuffer())

                with st.spinner("OCR en cours..."):
                    text = pdf_to_text_parallel(str(path))

                with st.spinner("Chunking..."):
                    chunks = chunk_text(text)

                with st.spinner("Embedding..."):
                    matrix = embed_chunks(chunks)

                st.session_state.chunks = chunks
                st.session_state.matrix = matrix

            st.success(f"{len(chunks)} chunks créés")

    # Chat
    if "chunks" in st.session_state:

        query = st.text_input("Pose ta question")

        if query:
            q_vec = embed_query(query)

            scores = st.session_state.matrix @ q_vec
            best_idx = np.argmax(scores)

            context = st.session_state.chunks[best_idx]

            llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)

            prompt = f"""
    Réponds uniquement avec ce contexte :

    {context}

    Question :
    {query}
    """

            response = llm.invoke(prompt)

            st.write("### Réponse")
            st.write(response.content)

            st.write("### Chunk utilisé")
            st.write(context)
