import unittest
from models.types import ToolCall, ModelResponse


class TestModelTypes(unittest.TestCase):

    def test_tool_call(self):
        tool = ToolCall(
            id="call_001",
            name="list_files",
            arguments={"directory": "."}
        )

        self.assertEqual(tool.id, "call_001")
        self.assertEqual(tool.name, "list_files")
        self.assertEqual(tool.arguments, {"directory": "."})

    def test_text_none_response(self):
        response = ModelResponse(model = "test-model", content = None)
        self.assertEqual(response.model, "test-model")
        self.assertIsNone(response.content)

    def test_single_tool_call_response(self):
        tool = ToolCall(
            id="call_001",
            name="list_files",
            arguments={"directory": "."}
        )

        response = ModelResponse(
            model="fake-model",
            content=None,
            tool_calls=[tool]
        )

        self.assertEqual(len(response.tool_calls), 1)
        self.assertEqual(response.tool_calls[0].name, "list_files")

    def test_multiple_tool_calls_response(self):
        tool1 = ToolCall(
            id="call_001",
            name="list_files",
            arguments={"directory": "."}
        )
        tool2 = ToolCall(
            id="call_002",
            name="get_file_size",
            arguments={"file_path": "example.txt"}
        )

        response = ModelResponse(
            model="fake-model",
            content=None,
            tool_calls=[tool1, tool2]
        )

        self.assertEqual(len(response.tool_calls), 2)
        self.assertEqual(response.tool_calls[0].name, "list_files")

    def test_tool_calls_have_independent_lists(self):
        tool1 = ToolCall(
            id="call_001",
            name="list_files",
            arguments={"directory": "."}
        )
        tool2 = ToolCall(
            id="call_002",
            name="get_file_size",
            arguments={"file_path": "example.txt"}
        )

        response1 = ModelResponse(
            model="fake-model"
        )

        response2 = ModelResponse(
            model="fake-model"
        )
        response1.tool_calls.append(tool1)

        self.assertEqual(len(response1.tool_calls), 1)
        self.assertEqual(len(response2.tool_calls), 0)
        self.assertEqual(response1.tool_calls[0].name, "list_files")

if __name__ == "__main__":
    unittest.main()
