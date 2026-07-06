import base64
import json
from pathlib import Path

import requests


class VisionEngine:

    def __init__(self, model="gemma3:4b"):

        self.model = model

        self.url = "http://localhost:11434/api/generate"

    def detect(self, image_path):

        image_path = Path(image_path)

        if not image_path.exists():
            raise FileNotFoundError(image_path)

        with open(image_path, "rb") as f:

            image = base64.b64encode(
                f.read()
            ).decode()

        prompt = """
You are an ecommerce product detector.

Analyze the image.

Return ONLY valid JSON.

Format:

{
  "product_name":"",
  "category":"",
  "keywords":[],
  "confidence":0
}
"""

        payload = {

            "model": self.model,

            "prompt": prompt,

            "images": [image],

            "stream": False

        }

        response = requests.post(

            self.url,

            json=payload,

            timeout=120

        )

        result = response.json()["response"]

        try:

            cleaned = result.strip()

            if cleaned.startswith("```json"):
                cleaned = cleaned.replace(
                    "```json",
                    "",
                    1
                )

            if cleaned.endswith("```"):
                cleaned = cleaned[:-3]

            cleaned = cleaned.strip()

            data = json.loads(cleaned)

            data["success"] = True

            return data

        except Exception:

            return {

                "success": False,

                "raw": result

            }