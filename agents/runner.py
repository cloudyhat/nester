from typing import Any
from models.base import Model
from models.types import ModelRequest
from agents.types import AgentDecision

class AgentRunner:
    def __init__(self, model: Model, max_iterations: int = 10):
        self.model = model
        self.max_iterations = max_iterations

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
    