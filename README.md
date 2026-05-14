# RAG-modular-rag-studio
A modular RAG experimentation platform built with Streamlit. Upload documents, test different chunking methods, select LLM providers, and interact with your knowledge base through chat.

# Backlog

| Task | Status |
|------|--------|
| Initial PDF processing pipeline (Docling OCR + RecursiveCharacterTextSplitter chunking) | ✅ Done |
| Build basic Streamlit interface with sidebar navigation | ✅ Done |
| Multi-page Streamlit interface | ✅ Done |
| Background document processing (job manager / async) | ✅ Done |
| Separate pipeline components (Parser, Chunker, Embedding) with their respective configuration | ✅ Done |
| OpenAI-compatible LLM integration for chat | 🚧 In Progress |
| Vector database integration (ChromaDB) | ⏳ Not Started |
| User session management | ⏳ Not Started |
| Ollama LLM integration for chat | ⏳ Not Started |
| First PyPI release (fixed parser + fixed chunking) | ⏳ Not Started |
| Support multiple parser engines | ⏳ Not Started |
| Add configurable parser selection in UI | ⏳ Not Started |
| Release with multiple parser support | ⏳ Not Started |
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
| `pipeline_config` | `dict` | Dictionary containing selected pipeline configuration |
| `parser_name` | `str` | Name of the selected parser |
| `parser_config` | `dict` | Configuration dictionary for the selected parser |
| `chunker_name` | `str` | Name of the selected chunking method |
| `chunker_config` | `dict` | Configuration dictionary for the selected chunking method |
| `embedding_name` | `str` | Name of the selected embedding model |
| `embedding_config` | `dict` | Configuration dictionary for the selected embedding model |
| `retrieval_config` | `dict` | Configuration dictionary for the selected retrieval parameters |
| `keys` | `dict` | Dictionary containing API keys, e.g., `{"OPENAI_API_KEY": "<your_api_key>"}` |
| `copied_dir` | `Path` | Directory where uploaded PDF files are copied for persistence |
| `output_dir` | `Path` | Directory where parsed output Markdown files are written |
| `parsing_results` | `dict` | Maps each file ID to its parsing metadata (filename, path, chunk count, etc.) |
| `current_job` | `ProcessingJob` | The current background processing job, which tracks the status of uploaded files and their parsing progress |
| `vector_store` | `dict` | Holds `chunks` (list of text chunks with metadata) and `matrix` (stacked embedding matrix used for similarity search) |
| `native_parser` | parser | PDF-to-Markdown converter using native (non-OCR) parsing |
| `ocr_parser` | parser | PDF-to-Markdown converter using OCR-based parsing |
| `parsers_logged` | `bool` | Whether the PDF parsers have been initialised and logged for this session |
| `embedder` | embedder | Loaded sentence-transformer model instance used to embed chunks and queries |
| `embeddings_logged` | `bool` | Whether the embedding model has been initialised and logged for this session |
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

# Contributing

As you can see, this framework aims to provide a highly modular and flexible RAG experimentation environment.

The goal is to make every pipeline component easily interchangeable and extensible (parsing, OCR, chunking, embedding, retrieval, vector stores, LLM providers). Because of this flexibility, the project requires many pre-implemented modules and integrations.

The architecture has been intentionally designed to be easy to extend, so feel free to contribute by opening PRs with:
- New parsing methods
- OCR engines
- Chunking strategies
- Embedding providers
- Retrieval techniques
- Experimental RAG ideas
- Performance improvements

Even small contributions are welcome 😊
