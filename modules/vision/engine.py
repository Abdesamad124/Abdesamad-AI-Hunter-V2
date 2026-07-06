import base64
import json
from pathlib import Path

import requests

from core.config import OLLAMA_URL, VISION_MODEL


class VisionEngine:

    def __init__(self):

        self.url = OLLAMA_URL

        self.model = VISION_MODEL

    def detect(self, image_path):

        image = Path(image_path)

        if not image.exists():

            raise FileNotFoundError(image)

        with open(image, "rb") as f:

            image64 = base64.b64encode(

                f.read()

            ).decode()

        prompt = """
You are an ecommerce product detector.

Analyze the image.

Return ONLY JSON.

Format:

{
    "product_name":"",
    "brand":"",
    "category":"",
    "material":"",
    "color":"",
    "target":"",
    "confidence":0,
    "keywords":[],
    "search_queries":[]
}

Rules:

Generate at least 3 search_queries.

Example:

[
"crochet tote bag",
"personalized crochet bag",
"handmade crochet shoulder bag"
]
"""

        payload = {

            "model": self.model,

            "prompt": prompt,

            "images": [

                image64

            ],

            "stream": False

        }

        response = requests.post(

            self.url,

            json=payload,

            timeout=180

        )

        result = response.json()["response"].strip()

        if result.startswith("```json"):

            result = result.replace(

                "```json",

                ""

            )

        if result.endswith("```"):

            result = result[:-3]

        data = json.loads(result)

        data["success"] = True

        return data