import unittest
from models.types import ToolCall
from tools.registry import ToolRegistry
from tools.executor import ToolExecutor
from tools.types import ToolExecutionResult

class TestToolExecutor(unittest.TestCase):
    def setUp(self):
        self.registry = ToolRegistry()
        self.calls = []

        def file_list(directory):
            self.calls.append(directory)
            return ["main.py", "utils.py"]

        self.registry.register("list_files", file_list)

        self.executor = ToolExecutor(self.registry)

    def test_list_files(self):

        tool_call = ToolCall(
            id="call_001",
            name="list_files",
            arguments={"directory": "src"}
        )

        result = self.executor.execute(tool_call)

        self.assertIsInstance(result, ToolExecutionResult)
        self.assertTrue(result.success)
        self.assertEqual(result.tool_call_id, "call_001")
        self.assertEqual(result.tool_name, "list_files")
        self.assertEqual(result.output, ["main.py", "utils.py"])

    def test_non_existent_tool(self):
        tool_call = ToolCall(
            id="call_002",
            name="unknown_tool",
            arguments={}
        )

        result = self.executor.execute(tool_call)

        self.assertIsInstance(result, ToolExecutionResult)
        self.assertFalse(result.success)
        self.assertEqual(result.tool_call_id, "call_002")
        self.assertEqual(result.tool_name, "unknown_tool")
        self.assertIsNone(result.output)
        print(result.error)

    def test_failing_tool(self):
        def failing_tool():
            raise RuntimeError("Tool failed")

        self.registry.register("failing_tool", failing_tool)

        tool_call = ToolCall(
            id="call_003",
            name="failing_tool",
            arguments={}
        )

        result = self.executor.execute(tool_call)

        self.assertIsInstance(result, ToolExecutionResult)
        self.assertFalse(result.success)
        self.assertEqual(result.tool_call_id, "call_003")
        self.assertEqual(result.tool_name, "failing_tool")
        self.assertIsNone(result.output)
        self.assertEqual(result.error, "Tool failed")
