from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

from core.base_search import BaseSearch
from core.config import USER_AGENT


class GoogleSearch(BaseSearch):

    def __init__(self):

        super().__init__()

    def search(self, query):

        try:

            headers = {

                "User-Agent": USER_AGENT

            }

            url = f"https://www.google.com/search?q={quote(query)}"

            response = requests.get(

                url,

                headers=headers,

                timeout=self.timeout

            )

            soup = BeautifulSoup(

                response.text,

                "lxml"

            )

            links = []

            for a in soup.select("a"):

                href = a.get("href")

                if not href:
                    continue

                if href.startswith("/url?q="):

                    href = href.replace(

                        "/url?q=",

                        ""

                    ).split("&")[0]

                    if href not in links:

                        links.append(href)

                if len(links) >= self.max_results:

                    break

            return self.success(

                "Google",

                links=links

            )

        except Exception as e:

            return self.failed(

                "Google",

                e

            )