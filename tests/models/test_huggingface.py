from models.config import ModelConfig
from models.huggingface import HuggingFaceModel
from models.types import ModelRequest


config = ModelConfig(
    model="openai/gpt-oss-120b:cerebras",
    temperature=0.7,
    max_tokens=500,
)

model = HuggingFaceModel(config)

request = ModelRequest(
    messages=[
        {
            "role": "user",
            "content": "Tell me a fun fact about the Eiffel Tower.",
        }
    ]
)

for chunk in model.stream(request):
    if chunk.reasoning:
        print(f"[reasoning] {chunk.reasoning}", end="")

    if chunk.content:
        print(chunk.content, end="")

    if chunk.finish_reason:
        print(f"\nFinished: {chunk.finish_reason}")

# print(response.content)
# print(response.model)
# print(response.usage)
# if response.metrics:
#     print(f"Latency: {response.metrics.latency_ms:.2f} ms")