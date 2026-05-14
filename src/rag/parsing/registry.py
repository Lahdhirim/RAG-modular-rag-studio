from src.rag.parsing.methods.docling import DoclingParser
from utils.schema import ConfigSchema

PARSER_REGISTRY = {
    ConfigSchema.DOCLING: DoclingParser,
}
