from dataclasses import dataclass
from typing import Any


@dataclass
class ModelRequest:
    messages: list[dict[str, Any]]
    model: str
    temperature: float = 1.0
    max_tokens: int | None = None


@dataclass
class ModelResponse:
    content: str
    model: str
    usage: dict[str, Any] | None = None