from modules.search.jumia import JumiaSearch
from modules.search.google import GoogleSearch
from modules.search.tiktok import TikTokSearch
from modules.search.facebook import FacebookSearch
from modules.search.google_images import GoogleImagesSearch

class SearchEngine:

    def __init__(self):

        self.engines = {

            "jumia": JumiaSearch(),

            "google": GoogleSearch(),
            "google_images": GoogleImagesSearch(),
            "tiktok": TikTokSearch(),

            "facebook": FacebookSearch()

        }

    def search(self, vision):

        queries = vision.get(

            "search_queries",

            vision.get("keywords", [])

        )

        if not queries:

            queries = [

                vision["product_name"]

            ]

        final = {}

        for name, engine in self.engines.items():

            best = None

            best_count = -1

            for q in queries:

                result = engine.search(q)

                if result["count"] > best_count:

                    best = result

                    best_count = result["count"]

            final[name] = best

        return final