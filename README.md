# RAG-modular-rag-studio
A modular RAG experimentation platform built with Streamlit. Upload documents, test different chunking methods, select LLM providers, and interact with your knowledge base through chat.

# Backlog

| Task | Status |
|------|--------|
| Initial PDF processing pipeline (Docling OCR + RecursiveCharacterTextSplitter chunking) | ✅ Done |
| Build basic Streamlit interface with sidebar navigation | ✅ Done |
| Multi-page Streamlit interface | ✅ Done |
| Background document processing (job manager / async) | ✅ Done |
| Separate pipeline components (Parser, Chunker, Embedding, Vector Store, Retrieval, LLM) with their respective configuration | 🚧 In Progress |
| Vector database integration (ChromaDB) | ⏳ Not Started |
| User session management | ⏳ Not Started |
| OpenAI-compatible LLM integration for chat | ⏳ Not Started |
| Ollama LLM integration for chat | ⏳ Not Started |
| First PyPI release (fixed OCR + fixed chunking) | ⏳ Not Started |
| Support multiple OCR engines | ⏳ Not Started |
| Add configurable OCR selection in UI | ⏳ Not Started |
| Release with multiple OCR support | ⏳ Not Started |
| Support multiple chunking strategies | ⏳ Not Started |
| Add configurable chunking strategy selection in UI | ⏳ Not Started |
| Release with multiple chunking strategies | ⏳ Not Started |

# Streamlit Session State Variables

All shared state is stored in Streamlit's `st.session_state` dictionary and is accessible across all pages.

| Variable | Type | Description |
|---|---|---|
| `authenticated` | `bool` | Whether the user has successfully logged in |
| `initialized` | `bool` | Whether the app-level initialization block has already run |
| `config` | `dict` | Application main configuration loaded from `config/config.json` |
| `keys` | `dict` | Dictionary containing API keys, e.g., `{"OPENAI_API_KEY": "<your_api_key>"}` |
| `copied_dir` | `Path` | Directory where uploaded PDF files are copied for persistence |
| `output_dir` | `Path` | Directory where parsed output Markdown files are written |
| `parsing_results` | `dict` | Maps each file ID to its parsing metadata (filename, path, chunk count, etc.) |
| `vector_store` | `dict` | Holds `chunks` (list of text chunks with metadata) and `matrix` (stacked embedding matrix used for similarity search) |
| `native_converter` | converter | PDF-to-Markdown converter using native (non-OCR) parsing |
| `ocr_converter` | converter | PDF-to-Markdown converter using OCR-based parsing |
| `converters_logged` | `bool` | Whether the PDF converters have been initialised and logged for this session |
| `embedding_model` | model | Loaded sentence-transformer model instance used to embed chunks and queries |
| `embeddings_logged` | `bool` | Whether the embedding model has been initialised and logged for this session |
| `current_job` | `ProcessingJob` | The current background processing job, which tracks the status of uploaded files and their parsing progress |
| `scanned_map` | `dict` | Maps each file ID to its scanned status (the choice is given by the user) |
| `chunker_method` | chunker | The chunking method selected by the user |
| `chunker_logged` | `bool` | Whether the chunking method has been initialised and logged for this session |

# Installation

### 1. Install `uv`

#### Linux / macOS
```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```
#### Windows
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone the repository and install dependencies
```bash
git clone https://github.com/Lahdhirim/RAG-modular-rag-studio.git
cd RAG-modular-rag-studio
uv sync
```
### 3. Run the application
```bash
uv run streamlit run RAG_Application.py
```


