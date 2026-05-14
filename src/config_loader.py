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


################## Main configuration ##################
AllowedParserNames = Literal["docling"]
AllowedChunkerNames = Literal["recursive_character"]
AllowedEmbeddingNames = Literal["hugging_face"]


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

    # Validate that exactly one method is enabled for parsing, chunking and embedding
    @model_validator(mode="after")
    def validate_configs(self):

        validate_single_enabled(self.parsing_config, "parser")

        validate_single_enabled(self.chunking_config, "chunker")

        validate_single_enabled(self.embedding_config, "embedding")

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


def load_config(path: str) -> StudioRAGConfig:
    try:
        with open(path, "r", encoding="utf-8") as f:
            config = json.load(f)
        return StudioRAGConfig(**config)

    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {path}")

    except Exception as e:
        raise ValueError(f"Invalid config: {e}")
