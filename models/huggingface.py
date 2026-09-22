import os
from openai import OpenAI
from .base import Model
from .types import ModelRequest, ModelResponse


class HuggingFaceModel(Model):

    def __init__(self):
        self.client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=os.getenv("HF_TOKEN"),
        )

    def generate(self, request: ModelRequest) -> ModelResponse:
        response = self.client.chat.completions.create(
            model=request.model,
            messages=request.messages,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )

        return ModelResponse(
            content=response.choices[0].message.content or "",
            model=response.model,
            usage=response.usage.model_dump() if response.usage else None,
        )