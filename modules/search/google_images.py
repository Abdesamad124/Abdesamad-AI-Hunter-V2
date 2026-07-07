from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

from core.base_search import BaseSearch
from core.config import USER_AGENT


class GoogleImagesSearch(BaseSearch):

    def __init__(self):
        super().__init__()

    def search(self, query):

        try:

            headers = {
                "User-Agent": USER_AGENT
            }

            url = f"https://www.google.com/search?tbm=isch&q={quote(query)}"

            response = requests.get(
                url,
                headers=headers,
                timeout=self.timeout
            )

            soup = BeautifulSoup(
                response.text,
                "lxml"
            )

            images = []

            for img in soup.select("img"):

                src = img.get("src")

                if not src:
                    continue

                if src.startswith("http"):

                    images.append({

                        "image": src

                    })

                if len(images) >= self.max_results:

                    break

            return self.success(

                "Google Images",

                products=images

            )

        except Exception as e:

            return self.failed(

                "Google Images",

                e
            )