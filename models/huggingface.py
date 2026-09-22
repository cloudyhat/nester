import os
from openai import OpenAI
from .base import Model
from .config import ModelConfig
from .types import ModelRequest, ModelResponse


class HuggingFaceModel(Model):

    def __init__(self, config: ModelConfig):
        self.config = config

        self.client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=os.getenv("HF_TOKEN"),
        )

    def generate(self, request: ModelRequest) -> ModelResponse:
        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=request.messages,
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens,
        )

        return ModelResponse(
            content=response.choices[0].message.content or "",
            model=response.model,
            usage=response.usage.model_dump() if response.usage else None,
        )