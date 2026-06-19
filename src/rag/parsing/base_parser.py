from abc import ABC, abstractmethod


class BaseParser(ABC):

    def __init__(self, params: dict | None = None):

        self.params = params or {}

    @abstractmethod
    def parse(self, file_path: str):
        # TODO: Add docstring
        pass
