import json
from typing import Any
from models.base import Model
from models.types import ModelRequest, ModelResponse
from agents.types import AgentDecision
from tools.executor import ToolExecutor

class AgentRunner:
    def __init__(self, model: Model, max_iterations: int = 10, executor: ToolExecutor | None = None):
        self.model = model
        self.max_iterations = max_iterations
        self.executor = executor

    def _build_assistant_tool_message(self, response: ModelResponse) -> dict[str, Any]:
        message = {
            "role": "assistant",
            "content": response.content,
            "tool_calls": [
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.name,
                        "arguments": json.dumps(tool_call.arguments),
                    },
                }
                for tool_call in response.tool_calls
            ],
        }
        return message

    def run(self, input_data: Any) -> AgentDecision:
        messages = input_data.get("messages", [])
        request = ModelRequest(messages=messages)
        response = self.model.generate(request)
        if response.tool_calls:
            return AgentDecision(
                kind="tool_call",
                tool_calls=response.tool_calls,
                content=response.content
            )
        return AgentDecision(kind="final", content=response.content)
    
    