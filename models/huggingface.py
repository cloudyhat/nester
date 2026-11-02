import os
import time
from openai import OpenAI
from .base import Model
from .config import ModelConfig
from .types import InferenceMetrics, ModelRequest, ModelResponse, ModelStreamChunk
from collections.abc import Iterator

class HuggingFaceModel(Model):

    def __init__(self, config: ModelConfig):
        self.config = config

        self.client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=os.getenv("HF_TOKEN"),
        )

    def generate(self, request: ModelRequest) -> ModelResponse:
        start = time.perf_counter()

        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=request.messages,
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens,
            stream=True,
        )

        for chunk in response:
            print(chunk)

        raise NotImplementedError

        latency_ms = (time.perf_counter() - start) * 1000

        return ModelResponse(
            content=response.choices[0].message.content or "",
            model=response.model,
            usage=response.usage.model_dump() if response.usage else None,
            metrics=InferenceMetrics(latency_ms=latency_ms,),
            
        )

    def stream(self, request: ModelRequest) -> Iterator[ModelStreamChunk]:
        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=request.messages,
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens,
            stream=True,
        )

        for chunk in response:
            delta = chunk.choices[0].delta

            yield ModelStreamChunk(
                content=delta.content,
                reasoning=getattr(delta, "reasoning", None),
                finish_reason=chunk.choices[0].finish_reason,
            )