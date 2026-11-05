from models.types import ToolCall
from tools.registry import ToolRegistry
from tools.types import ToolExecutionResult

class ToolExecutor:
    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute(self, tool_call: ToolCall):
        try:
            tool = self.registry.get(tool_call.name)
            tool_arg = tool_call.arguments if tool_call.arguments else {}
            output = tool(**tool_arg)
            return ToolExecutionResult(
                tool_call_id=tool_call.id,
                tool_name=tool_call.name,
                output=output
            )
        except Exception as e:
            return ToolExecutionResult(
                tool_call_id=tool_call.id,
                tool_name=tool_call.name,
                output=None,
                error=str(e),
                success=False
            )