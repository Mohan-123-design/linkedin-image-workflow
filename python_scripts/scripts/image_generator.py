import requests
import json
import base64
import subprocess
import os

PROJECT_ID = "triple-pottery-479908-n7"
LOCATION = "us-central1"
MODEL_ID = "gemini-2.5-flash-image"

def get_access_token():
    result = subprocess.run(
        ["gcloud", "auth", "application-default", "print-access-token"],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()

def generate_image(prompt, file_name):
    token = get_access_token()

    url = (
        f"https://{LOCATION}-aiplatform.googleapis.com/v1/"
        f"projects/{PROJECT_ID}/locations/{LOCATION}/"
        f"publishers/google/models/{MODEL_ID}:predict"
    )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "instances": [
            {
                "prompt": prompt
            }
        ],
        "parameters": {
            "aspectRatio": "1:1"
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(response.text)

    image_base64 = response.json()["predictions"][0]["bytesBase64Encoded"]
    image_bytes = base64.b64decode(image_base64)

    os.makedirs("output/images", exist_ok=True)
    path = f"output/images/{file_name}.png"

    with open(path, "wb") as f:
        f.write(image_bytes)

    return path
