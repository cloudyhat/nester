from dataclasses import dataclass, field
from typing import Any

@dataclass
class InferenceMetrics:
    latency_ms : float 

@dataclass
class ModelRequest:
    messages: list[dict[str, Any]]

@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict[str, Any]

@dataclass
class ModelResponse:
    model: str
    content: str | None = None
    tool_calls: list[ToolCall] = field(default_factory=list)
    usage: dict[str, Any] | None = None
    metrics: InferenceMetrics | None = None

@dataclass
class ModelStreamChunk:
    content: str | None = None
    reasoning: str | None = None
    finish_reason: str | None = None