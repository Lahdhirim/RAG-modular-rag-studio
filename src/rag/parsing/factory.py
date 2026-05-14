from src.config_loader import ParsingMethodConfig
from src.rag.parsing.registry import PARSER_REGISTRY
from src.utils.logger_config import logger


def init_parser(
    parser_name: str, parser_config: ParsingMethodConfig, ocr: bool = False
):

    parser_instance = PARSER_REGISTRY.get(parser_name)

    if not parser_instance:
        raise ValueError(f"Unsupported parser: {parser_name}")

    logger.info(
        f"Selected parser: {parser_name} | Config: {parser_config} | OCR: {ocr}"
    )
    return parser_instance(
        params=parser_config.params,
        ocr=ocr,
    )
