from abc import ABC, abstractmethod

from .types import ModelRequest, ModelResponse


class Model(ABC):

    @abstractmethod
    def generate(self, request: ModelRequest) -> ModelResponse:
        """Generate a response from the model."""
        pass