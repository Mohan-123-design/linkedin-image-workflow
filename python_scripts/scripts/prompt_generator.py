import requests
import os

API_KEY = os.getenv("PERPLEXITY_API_KEY")

def generate_prompt(content):
    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "user",
                "content": f"{content} - create an image prompt in 1:1 ratio for LinkedIn post"
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()["choices"][0]["message"]["content"]
