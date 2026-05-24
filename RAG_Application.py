import os
from pathlib import Path
from typing import Optional

import streamlit as st
from dotenv import load_dotenv

from src.config_loader import (
    ChunkingMethodConfig,
    EmbeddingMethodConfig,
    LLMProviderConfig,
    ParsingMethodConfig,
    load_config,
)
from src.rag.chunking.factory import init_chunker
from src.rag.embedding.factory import init_embedding
from src.rag.llms.factory import init_chat_llm
from src.rag.parsing.factory import init_parser
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
def init_native_parser(parser_name: str, parser_config: ParsingMethodConfig):
    return init_parser(parser_name=parser_name, parser_config=parser_config, ocr=False)


@st.cache_resource
def init_ocr_parser(parser_name: str, parser_config: ParsingMethodConfig):
    return init_parser(parser_name=parser_name, parser_config=parser_config, ocr=True)


@st.cache_resource
def init_chunker_method(chunker_name: str, chunker_config: ChunkingMethodConfig):
    return init_chunker(chunker_name=chunker_name, chunker_config=chunker_config)


@st.cache_resource
def init_embedding_method(embedding_name: str, embedding_config: EmbeddingMethodConfig):
    return init_embedding(
        embedding_name=embedding_name, embedding_config=embedding_config
    )


@st.cache_resource
def init_selected_chat_llm(
    llm_provider_name: str,
    llm_provider_config: LLMProviderConfig,
    api_key: Optional[str] = None,
):
    return init_chat_llm(
        llm_provider_name=llm_provider_name,
        llm_provider_config=llm_provider_config,
        api_key=api_key,
    )


# Initialize session state and logging
if SessionStateSchema.INITIALIZED not in st.session_state:
    # Set up logging
    logger.info("Starting the RAG studio...")

    # Load configuration
    config_path = Path("config/config.json")
    config = load_config(config_path)
    logger.info(f"Loaded configuration from {config_path}: {config}")

    # Get selected methods from config
    parser_name, parser_cfg = config.get_selected_parser()
    logger.info(f"Selected parser: {parser_name} | Config: {parser_cfg}")

    chunker_name, chunker_cfg = config.get_selected_chunker()
    logger.info(f"Selected chunker: {chunker_name} | Config: {chunker_cfg}")

    embedding_name, embedding_cfg = config.get_selected_embedder()
    logger.info(
        f"Selected embedding method: {embedding_name} | Config: {embedding_cfg}"
    )

    llm_provider_name, llm_provider_cfg = config.get_selected_llm_provider()
    logger.info(
        f"Selected LLM provider: {llm_provider_name} | Config: {llm_provider_cfg}"
    )

    # Prepare directories
    COPIED_DIR = Path(config.directory_config.copied_pdfs_dir)
    OUTPUT_DIR = Path(config.directory_config.parsing_outputs_dir)
    COPIED_DIR.mkdir(exist_ok=True, parents=True)
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    logger.info(f"Created directories: {COPIED_DIR}, {OUTPUT_DIR}")

    # Load environment variables
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    logger.info("Loaded environment variables.")

    # Store in session state
    st.session_state[SessionStateSchema.CONFIG] = config
    st.session_state[SessionStateSchema.PIPELINE_CONFIG] = {
        SessionStateSchema.PARSER_NAME: parser_name,
        SessionStateSchema.PARSER_CONFIG: parser_cfg,
        SessionStateSchema.CHUNKER_NAME: chunker_name,
        SessionStateSchema.CHUNKER_CONFIG: chunker_cfg,
        SessionStateSchema.EMBEDDING_NAME: embedding_name,
        SessionStateSchema.EMBEDDING_CONFIG: embedding_cfg,
        SessionStateSchema.RETRIEVAL_CONFIG: config.retrieval_config,
        SessionStateSchema.LLM_PROVIDER_NAME: llm_provider_name,
        SessionStateSchema.LLM_PROVIDER_CONFIG: llm_provider_cfg,
    }
    st.session_state[SessionStateSchema.COPIED_DIR] = COPIED_DIR
    st.session_state[SessionStateSchema.OUTPUT_DIR] = OUTPUT_DIR
    st.session_state[SessionStateSchema.PARSING_RESULTS] = {}
    st.session_state[SessionStateSchema.CURRENT_JOB] = None
    st.session_state[SessionStateSchema.VECTOR_STORE] = {"chunks": [], "matrix": None}
    st.session_state[SessionStateSchema.INITIALIZED] = True

# Initialize parsers
native_parser = init_native_parser(
    parser_name=st.session_state[SessionStateSchema.PIPELINE_CONFIG][
        SessionStateSchema.PARSER_NAME
    ],
    parser_config=st.session_state[SessionStateSchema.PIPELINE_CONFIG][
        SessionStateSchema.PARSER_CONFIG
    ],
)
ocr_parser = init_ocr_parser(
    parser_name=st.session_state[SessionStateSchema.PIPELINE_CONFIG][
        SessionStateSchema.PARSER_NAME
    ],
    parser_config=st.session_state[SessionStateSchema.PIPELINE_CONFIG][
        SessionStateSchema.PARSER_CONFIG
    ],
)
if SessionStateSchema.PARSERS_LOGGED not in st.session_state:
    st.session_state[SessionStateSchema.NATIVE_PARSER] = native_parser
    st.session_state[SessionStateSchema.OCR_PARSER] = ocr_parser
    st.session_state[SessionStateSchema.PARSERS_LOGGED] = True
    logger.info(
        f"Initialized document parsers: {st.session_state[SessionStateSchema.PIPELINE_CONFIG][SessionStateSchema.PARSER_NAME]}"
    )

# Initialize chunker
chunker_method = init_chunker_method(
    chunker_name=st.session_state[SessionStateSchema.PIPELINE_CONFIG][
        SessionStateSchema.CHUNKER_NAME
    ],
    chunker_config=st.session_state[SessionStateSchema.PIPELINE_CONFIG][
        SessionStateSchema.CHUNKER_CONFIG
    ],
)
if SessionStateSchema.CHUNKER_LOGGED not in st.session_state:
    st.session_state[SessionStateSchema.CHUNKER_METHOD] = chunker_method
    st.session_state[SessionStateSchema.CHUNKER_LOGGED] = True
    logger.info(
        f"Initialized chunker method: {st.session_state[SessionStateSchema.PIPELINE_CONFIG][SessionStateSchema.CHUNKER_NAME]}"
    )

# Initialize embeddings model
embedder = init_embedding_method(
    embedding_name=st.session_state[SessionStateSchema.PIPELINE_CONFIG][
        SessionStateSchema.EMBEDDING_NAME
    ],
    embedding_config=st.session_state[SessionStateSchema.PIPELINE_CONFIG][
        SessionStateSchema.EMBEDDING_CONFIG
    ],
)
if SessionStateSchema.EMBEDDINGS_LOGGED not in st.session_state:
    st.session_state[SessionStateSchema.EMBEDDER] = embedder
    st.session_state[SessionStateSchema.EMBEDDINGS_LOGGED] = True
    logger.info(
        f"Initialized embeddings model: {st.session_state[SessionStateSchema.PIPELINE_CONFIG][SessionStateSchema.EMBEDDING_NAME]}"
    )

# Initialize LLM
if (
    st.session_state[SessionStateSchema.PIPELINE_CONFIG][
        SessionStateSchema.LLM_PROVIDER_NAME
    ]
    is None
):
    logger.warning(
        "No LLM provider selected in the configuration. Chat functionality will be unavailable."
    )
    chat_llm = None
else:
    chat_llm = init_selected_chat_llm(
        llm_provider_name=st.session_state[SessionStateSchema.PIPELINE_CONFIG][
            SessionStateSchema.LLM_PROVIDER_NAME
        ],
        llm_provider_config=st.session_state[SessionStateSchema.PIPELINE_CONFIG][
            SessionStateSchema.LLM_PROVIDER_CONFIG
        ],
        api_key=OPENAI_API_KEY,
    )
if SessionStateSchema.LLM_LOGGED not in st.session_state:
    st.session_state[SessionStateSchema.CHAT_LLM] = chat_llm
    st.session_state[SessionStateSchema.LLM_LOGGED] = True
    logger.info(
        f"Initialized Chat LLM: {st.session_state[SessionStateSchema.PIPELINE_CONFIG][SessionStateSchema.LLM_PROVIDER_NAME]}"
    )

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

### 3. 💬 Chat
Go to the **Chat** page to:
            
    - Ask questions about your documents  
    - Retrieve the most relevant content  
                      
---

### 4. 📚 View Documents
Visit the **Documents** page to:
            
    - See parsed results  
    - Explore generated chunks  

---

💡 **Tip:** Upload your documents before starting a chat session.
""")
