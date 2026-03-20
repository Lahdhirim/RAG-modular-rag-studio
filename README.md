# RAG-modular-rag-studio
A modular RAG experimentation platform built with Streamlit. Upload documents, test different chunking methods, select LLM providers, and interact with your knowledge base through chat.

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
uv run streamlit run main.py
```


