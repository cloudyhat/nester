from dataclasses import dataclass
from typing import Any

@dataclass
class ToolExecutionResult:
    tool_call_id: str
    tool_name: str
    output: Any
    error: str | None = None
    success: bool = True