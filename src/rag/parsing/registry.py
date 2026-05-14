from src.rag.parsing.methods.docling import DoclingParser
from src.utils.schema import ConfigSchema

PARSER_REGISTRY = {
    ConfigSchema.DOCLING: DoclingParser,
}
