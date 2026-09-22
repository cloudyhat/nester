from models.huggingface import HuggingFaceModel
from models.types import ModelRequest


model = HuggingFaceModel()

request = ModelRequest(
    model="openai/gpt-oss-120b:cerebras",
    messages=[
        {
            "role": "user",
            "content": "Tell me a fun fact about the Eiffel Tower.",
        }
    ],
)

response = model.generate(request)

print(response.content)
print(response.model)
print(response.usage)