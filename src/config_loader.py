import json
from typing import Any, Dict, Literal, Optional

from pydantic import BaseModel, Field, model_validator

AllowedParserNames = Literal["docling"]


class ParsingMethodConfig(BaseModel):
    enabled: bool = Field(..., description="Whether the parsing method is enabled")
    params: Optional[Dict[str, Any]] = Field(
        default=None, description="Parameters specific to the selected parsing method"
    )


class ParsingConfig(BaseModel):
    enable_gpu: Optional[bool] = Field(
        default=False, description="Enable GPU acceleration"
    )

    method_config: Dict[AllowedParserNames, ParsingMethodConfig] = Field(
        ..., description="Parsing method choice and configuration"
    )

    @model_validator(mode="after")
    def check_single_parser_enabled(self):
        enabled = [name for name, cfg in self.method_config.items() if cfg.enabled]

        if len(enabled) != 1:
            raise ValueError(f"Exactly ONE Parser must be enabled, got: {enabled}")

        return self

    def get_selected_parser(self):
        for name, cfg in self.method_config.items():
            if cfg.enabled:
                return name, cfg


class ChunkingMethodConfig(BaseModel):
    enabled: bool = Field(..., description="Whether the chunking method is enabled")
    params: Optional[Dict[str, Any]] = Field(
        default=None, description="Parameters specific to the selected chunking method"
    )


class RAGConfig(BaseModel):
    chunking_config: Dict[str, ChunkingMethodConfig] = Field(
        ..., description="Chunking configuration"
    )
    embedding_model: str = Field(..., description="Embedding model name")
    top_k: int = Field(default=5, description="Number of retrieved chunks")
    similarity_threshold: float = Field(
        default=0.7, description="Minimum similarity threshold"
    )

    @model_validator(mode="after")
    def check_single_chunking_enabled(self):
        enabled = [name for name, cfg in self.chunking_config.items() if cfg.enabled]

        if len(enabled) != 1:
            raise ValueError(
                f"Exactly ONE chunking method must be enabled, got: {enabled}"
            )

        return self

    def get_selected_chunker(self):
        for name, cfg in self.chunking_config.items():
            if cfg.enabled:
                return name, cfg


class DirectoryConfig(BaseModel):
    copied_pdfs_dir: Optional[str] = Field(
        default="outputs/copied_pdfs", description="Directory for copied PDFs"
    )
    parsing_outputs_dir: Optional[str] = Field(
        default="outputs/parsing_outputs", description="Directory for parsing outputs"
    )


class StudioConfig(BaseModel):
    directory_config: DirectoryConfig = Field(
        ..., description="Directory paths configuration"
    )
    parsing_config: ParsingConfig = Field(
        ..., description="Document parsing configuration"
    )
    rag_config: RAGConfig = Field(..., description="RAG configuration")


def load_config(path: str) -> StudioConfig:
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return StudioConfig(**data)

    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {path}")

    except Exception as e:
        raise ValueError(f"Invalid config: {e}")
