import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from src.config_loader import ParsingConfig, load_config
from src.rag.embeddings import load_embeddings_model
from src.rag.processing import get_converter
from src.utils.logger_config import logger
from src.utils.schema import SessionStateSchema

# Set Streamlit page configuration
st.set_page_config(page_title="RAG Studio", layout="wide", page_icon="assets/logo.png")
st.title("📄 RAG Studio")
st.sidebar.image("assets/logo.png", width=120)

# Authentication state management
if st.session_state.get(SessionStateSchema.AUTHENTICATED, False):
    st.sidebar.success("✅ Logged in")

    if st.sidebar.button("Logout"):
        st.session_state[SessionStateSchema.AUTHENTICATED] = False
        st.rerun()
else:
    st.sidebar.warning("🔒 Not logged in")


@st.cache_resource
def get_native_converter(parsing_config: ParsingConfig):
    return get_converter(ocr=False, parsing_config=parsing_config)


@st.cache_resource
def get_ocr_converter(parsing_config: ParsingConfig):
    return get_converter(ocr=True, parsing_config=parsing_config)


@st.cache_resource
def get_embeddings(model_name: str):
    return load_embeddings_model(model_name=model_name)


# Initialize session state and logging
if SessionStateSchema.INITIALIZED not in st.session_state:
    # Set up logging
    logger.info("Starting the RAG studio...")

    # Load configuration
    config_path = Path("config/config.json")
    config = load_config(config_path)
    logger.info(f"Loaded configuration from {config_path}: {config}")

    # Prepare directories
    COPIED_DIR = Path(config.directory_config.copied_pdfs_dir)
    OUTPUT_DIR = Path(config.directory_config.parsing_outputs_dir)
    COPIED_DIR.mkdir(exist_ok=True, parents=True)
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    logger.info(f"Created directories: {COPIED_DIR}, {OUTPUT_DIR}")

    # Load environment variables
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    logger.info("Loaded environment variables.")

    # Store in session state
    st.session_state[SessionStateSchema.CONFIG] = config
    st.session_state[SessionStateSchema.KEYS] = {"OPENAI_API_KEY": OPENAI_API_KEY}
    st.session_state[SessionStateSchema.COPIED_DIR] = COPIED_DIR
    st.session_state[SessionStateSchema.OUTPUT_DIR] = OUTPUT_DIR
    st.session_state[SessionStateSchema.PARSING_RESULTS] = {}
    st.session_state[SessionStateSchema.CURRENT_JOB] = None
    st.session_state[SessionStateSchema.VECTOR_STORE] = {"chunks": [], "matrix": None}
    st.session_state[SessionStateSchema.INITIALIZED] = True

# Initialize converters
native_converter = get_native_converter(
    parsing_config=st.session_state[SessionStateSchema.CONFIG].parsing_config
)
ocr_converter = get_ocr_converter(
    parsing_config=st.session_state[SessionStateSchema.CONFIG].parsing_config
)
if SessionStateSchema.CONVERTERS_LOGGED not in st.session_state:
    st.session_state[SessionStateSchema.NATIVE_CONVERTER] = native_converter
    st.session_state[SessionStateSchema.OCR_CONVERTER] = ocr_converter
    logger.info("Initialized document converters.")
    st.session_state[SessionStateSchema.CONVERTERS_LOGGED] = True

# Initialize embeddings model
model = get_embeddings(
    model_name=st.session_state[SessionStateSchema.CONFIG].rag_config.embedding_model
)
if SessionStateSchema.EMBEDDINGS_LOGGED not in st.session_state:
    st.session_state[SessionStateSchema.EMBEDDING_MODEL] = model
    logger.info("Initialized embeddings model.")
    st.session_state[SessionStateSchema.EMBEDDINGS_LOGGED] = True

# Streamlit UI
st.markdown("""
Welcome to **RAG Studio** 👋  

This application lets you upload PDF documents, extract and chunk their content, and ask questions using a **Retrieval-Augmented Generation (RAG)** approach.

---

## Getting Started

### 1. 🔐 Login
Use the sidebar to log in:
            
    - Username: `admin`  
    - Password: `securepassword`

---

### 2. 📤 Upload Documents
Go to the **Upload** page:
            
    - Upload your PDF files  
    - Specify whether they are scanned or native. The app will handle text extraction accordingly  

---

### 3. 📚 View Documents
Visit the **Documents** page to:
            
    - See parsed results  
    - Explore generated chunks  

---

### 4. 💬 Chat
Go to the **Chat** page to:
            
    - Ask questions about your documents  
    - Retrieve the most relevant content  

---

💡 **Tip:** Upload your documents before starting a chat session.
""")
