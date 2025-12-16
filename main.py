import base64

from openai import OpenAI

from prompt import prompt

api_key = "EMPTY"
api_base = "http://localhost:8000/v1"
model = "Qwen/Qwen2.5-VL-3B-Instruct"
max_tokens = 192
min_pixels = 3136  # 3 * 28 * 28
max_pixels = 12845056  # 16384 * 28 * 28


client = OpenAI(api_key=api_key, base_url=api_base)

image_path = "product_test_samples/sample20.jpg"

with open(image_path, "rb") as f:
    b64_data = base64.b64encode(f.read()).decode("utf-8")
    b64_data = "data:image;base64," + b64_data


response = client.chat.completions.create(
    model=model,
    max_tokens=max_tokens,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": b64_data,
                    },
                    "min_pixels": min_pixels,
                    "max_pixels": max_pixels,
                },
                {"type": "text", "text": prompt},
            ],
        },
    ],
)

raw_text = response.choices[0].message.content
print(f"image_path: {image_path}")
print(raw_text)
