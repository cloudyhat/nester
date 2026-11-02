from dataclasses import dataclass, field
from typing import Literal
from models.types import ToolCall

@dataclass
class AgentDecision:
    kind: Literal["final", "tool_call"]
    content: str | None = None
    tool_calls: list[ToolCall] = field(default_factory=list)