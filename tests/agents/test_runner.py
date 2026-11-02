import unittest

from agents.runner import AgentRunner
from models.types import ModelRequest, ModelResponse, ToolCall


class FakeModel:
    def __init__(self, response):
        self.response = response

    def generate(self, request: ModelRequest):
        self.last_request = request
        return self.response


class TestAgentRunner(unittest.TestCase):

    def test_final_response(self):
        fake_response = ModelResponse(
            model="fake-model",
            content="Hello from Nester!"
        )
        runner = AgentRunner(model=FakeModel(fake_response))

        result = runner.run({
            "messages": [
                {"role": "user", "content": "Hello"}
            ]
        })

        self.assertEqual(result.kind, "final")
        self.assertEqual(result.content, "Hello from Nester!")
        self.assertEqual(
            runner.model.last_request.messages,
            [{"role": "user", "content": "Hello"}]
        )

    def test_tool_call_response(self):
        fake_response = ModelResponse(
            model="fake-model",
            content=None,
            tool_calls=[
                ToolCall(
                    id="call_001",
                    name="list_files",
                    arguments={"directory": "."}
                )
            ]
        )

        runner = AgentRunner(model=FakeModel(fake_response))

        result = runner.run({
            "messages": [
                {"role": "user", "content": "Hello"}
            ]
        })

        self.assertEqual(result.kind, "tool_call")
        self.assertEqual(len(result.tool_calls), 1)
        self.assertEqual(result.tool_calls[0].name, "list_files")
        self.assertEqual(result.tool_calls[0].id, "call_001")
        self.assertEqual(
            result.tool_calls[0].arguments,
            {"directory": "."}
        )


if __name__ == "__main__":
    unittest.main()
