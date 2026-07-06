from urllib.parse import quote

import requests
from bs4 import BeautifulSoup


class GoogleSearch:

    def search(self, query):

        headers = {

            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/137.0 Safari/537.36"
            )

        }

        url = f"https://www.google.com/search?q={quote(query)}"

        response = requests.get(

            url,

            headers=headers,

            timeout=15

        )

        soup = BeautifulSoup(response.text, "lxml")

        links = []

        for a in soup.select("a"):

            href = a.get("href")

            if not href:
                continue

            if href.startswith("/url?q="):

                href = href.replace("/url?q=", "").split("&")[0]

                links.append(href)

        return {

            "platform": "Google",

            "found": len(links) > 0,

            "count": len(links),

            "links": links[:10]

        }