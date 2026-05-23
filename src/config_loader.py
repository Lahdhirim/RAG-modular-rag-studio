import json
from typing import Any, Dict, Literal, Optional

from pydantic import BaseModel, Field, model_validator


def validate_single_enabled(config_dict, component_name):
    """Utility function to validate that exactly one method is enabled in a given config dictionary."""

    enabled = [name for name, cfg in config_dict.items() if cfg.enabled]

    if len(enabled) != 1:
        raise ValueError(
            f"Exactly ONE {component_name} must be enabled, got: {enabled}"
        )


def validate_max_one_enabled(config_dict, component_name):
    """Utility function to validate that at most one method is enabled in a given config dictionary."""

    enabled = [name for name, cfg in config_dict.items() if cfg.enabled]

    if len(enabled) > 1:
        raise ValueError(f"At most ONE {component_name} can be enabled, got: {enabled}")


################## Directory Configuration ##################
class DirectoryConfig(BaseModel):
    copied_pdfs_dir: Optional[str] = Field(
        default="outputs/copied_pdfs", description="Directory for copied PDFs"
    )
    parsing_outputs_dir: Optional[str] = Field(
        default="outputs/parsing_outputs", description="Directory for parsing outputs"
    )


################## Parsing Configuration ##################
class ParsingMethodConfig(BaseModel):
    enabled: bool = Field(..., description="Whether the parsing method is enabled")
    params: Optional[Dict[str, Any]] = Field(
        default=None, description="Parameters specific to the selected parsing method"
    )


################## Chunking Configuration ##################
class ChunkingMethodConfig(BaseModel):
    enabled: bool = Field(..., description="Whether the chunking method is enabled")
    params: Optional[Dict[str, Any]] = Field(
        default=None, description="Parameters specific to the selected chunking method"
    )


################## Embedding Configuration ##################
class EmbeddingMethodConfig(BaseModel):
    enabled: bool = Field(..., description="Whether the embedding method is enabled")
    params: Optional[Dict[str, Any]] = Field(
        default=None, description="Parameters specific to the selected embedding method"
    )


################## Retrieval Configuration ##################
class RetrievalConfig(BaseModel):
    top_k: Optional[int] = Field(default=5, description="Number of retrieved chunks")
    similarity_threshold: Optional[float] = Field(
        default=0.7, description="Minimum similarity threshold"
    )


################## LLM Provider Configuration ##################
class LLMProviderConfig(BaseModel):
    enabled: bool = Field(..., description="Whether the LLM provider is enabled")
    model_name: Optional[str] = Field(
        default="gpt-4o-mini", description="Name of the LLM model to use"
    )
    base_url: Optional[str] = Field(
        default=None, description="Base URL for provider endpoint"
    )
    temperature: Optional[float] = Field(
        default=0, description="Temperature setting for the LLM"
    )
    system_prompt: Optional[str] = Field(
        default="You are a helpful assistant for answering questions based on the provided context. Always use the provided context to answer questions and do not make up information. If you don't know the answer, say you don't know.",
        description="System prompt to guide the LLM's behavior",
    )


################## Main configuration ##################
AllowedParserNames = Literal["docling"]
AllowedChunkerNames = Literal["recursive_character"]
AllowedEmbeddingNames = Literal["hugging_face"]
AllowedLLMProviders = Literal["openai"]


class StudioRAGConfig(BaseModel):
    directory_config: DirectoryConfig = Field(
        ..., description="Directory paths configuration"
    )
    parsing_config: Dict[AllowedParserNames, ParsingMethodConfig] = Field(
        ..., description="Document parsing configuration"
    )
    chunking_config: Dict[AllowedChunkerNames, ChunkingMethodConfig] = Field(
        ..., description="Chunking configuration"
    )
    embedding_config: Dict[AllowedEmbeddingNames, EmbeddingMethodConfig] = Field(
        ..., description="Embedding configuration"
    )
    retrieval_config: RetrievalConfig = Field(
        ..., description="Retrieval configuration"
    )
    llm_config: Dict[AllowedLLMProviders, LLMProviderConfig] = Field(
        ..., description="LLM provider configuration"
    )

    # Validate that exactly one method is enabled for parsing, chunking, embedding and LLM provider
    @model_validator(mode="after")
    def validate_configs(self):

        validate_single_enabled(self.parsing_config, "parser")

        validate_single_enabled(self.chunking_config, "chunker")

        validate_single_enabled(self.embedding_config, "embedding")

        validate_max_one_enabled(self.llm_config, "LLM provider")

        return self

    # Get the selected parser and its config
    def get_selected_parser(self):
        for name, cfg in self.parsing_config.items():
            if cfg.enabled:
                return name, cfg

    # Get the selected chunking method and its config
    def get_selected_chunker(self):
        for name, cfg in self.chunking_config.items():
            if cfg.enabled:
                return name, cfg

    # Get the selected embedding method and its config
    def get_selected_embedder(self):
        for name, cfg in self.embedding_config.items():
            if cfg.enabled:
                return name, cfg

    # Get the selected LLM provider and its config
    def get_selected_llm_provider(self):
        for name, cfg in self.llm_config.items():
            if cfg.enabled:
                return name, cfg
        return None, None


def load_config(path: str) -> StudioRAGConfig:
    try:
        with open(path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return StudioRAGConfig(**config)

    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {path}")

    except Exception as e:
        raise ValueError(f"Invalid config: {e}")
