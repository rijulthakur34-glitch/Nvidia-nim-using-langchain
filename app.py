from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("NVIDIA_API_KEY"))
print(len(os.getenv("NVIDIA_API_KEY")) if os.getenv("NVIDIA_API_KEY") else "Key not found")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

print("Sending request to Nvidia API...")

completion = client.chat.completions.create(
    model="meta/llama-3.1-70b-instruct",
    messages=[
        {
            "role": "user",
            "content": "Provide me an essay on ML"
        }
    ],
    temperature=0.2,
    top_p=0.7,
    max_tokens=1024,
    stream=False,
)

print(completion.choices[0].message.content)
