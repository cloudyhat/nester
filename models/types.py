from dataclasses import dataclass
from typing import Any


@dataclass
class ModelRequest:
    messages: list[dict[str, Any]]


@dataclass
class ModelResponse:
    content: str
    model: str
    usage: dict[str, Any] | None = None