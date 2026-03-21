import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from src.config_loader import load_config
from src.rag.embeddings import load_embeddings_model
from src.rag.processing import get_converter
from src.utils.logger_config import logger

# Set Streamlit page configuration
st.set_page_config(page_title="Simple RAG", layout="wide")

# Authentication state management
if st.session_state.get("authenticated", False):
    st.sidebar.success("✅ Logged in")

    if st.sidebar.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()
else:
    st.sidebar.warning("🔒 Not logged in")


@st.cache_resource
def get_native_converter():
    return get_converter(ocr=False)


@st.cache_resource
def get_ocr_converter():
    return get_converter(ocr=True)


@st.cache_resource
def get_embeddings():
    return load_embeddings_model()


# Initialize session state and logging
if "initialized" not in st.session_state:
    # Set up logging
    logger.info("Starting the Simple RAG application...")

    # Prepare directories
    COPIED_DIR = Path("outputs/copied_pdfs")
    OUTPUT_DIR = Path("outputs/ocr_outputs")

    COPIED_DIR.mkdir(exist_ok=True, parents=True)
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    logger.info(f"Created directories: {COPIED_DIR}, {OUTPUT_DIR}")

    # Load environment variables
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    logger.info("Loaded environment variables.")

    # Load configuration
    config_path = Path("config/config.json")
    config = load_config(config_path)
    logger.info(f"Loaded configuration from {config_path}: {config}")

    # Store in session state
    st.session_state["config"] = config
    st.session_state["COPIED_DIR"] = COPIED_DIR
    st.session_state["OUTPUT_DIR"] = OUTPUT_DIR
    st.session_state["parsing_results"] = {}
    st.session_state["vector_store"] = {"chunks": [], "matrix": None}
    st.session_state["initialized"] = True

# Initialize converters
native_converter = get_native_converter()
ocr_converter = get_ocr_converter()
if "converters_logged" not in st.session_state:
    st.session_state["native_converter"] = native_converter
    st.session_state["ocr_converter"] = ocr_converter
    logger.info("Initialized document converters.")
    st.session_state["converters_logged"] = True

# Initialize embeddings model
model = get_embeddings()
if "embeddings_logged" not in st.session_state:
    st.session_state["embedding_model"] = model
    logger.info("Initialized embeddings model.")
    st.session_state["embeddings_logged"] = True

# Streamlit UI
st.title("📄 Simple RAG")
st.write("Use the sidebar to navigate")
