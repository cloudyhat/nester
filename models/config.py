from dataclasses import dataclass


@dataclass
class ModelConfig:
    model: str
    temperature: float = 1.0
    max_tokens: int | None = None