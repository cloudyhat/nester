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

response = model.generate(request)

print(response.content)
print(response.model)
print(response.usage)