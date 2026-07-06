from modules.search.jumia import JumiaSearch
from modules.search.google import GoogleSearch
from modules.search.tiktok import TikTokSearch
from modules.search.facebook import FacebookSearch


class SearchEngine:

    def __init__(self):

        self.jumia = JumiaSearch()

        self.google = GoogleSearch()

        self.tiktok = TikTokSearch()

        self.facebook = FacebookSearch()

    def search(self, query):

        return {

            "jumia": self.jumia.search(query),

            "google": self.google.search(query),

            "tiktok": self.tiktok.search(query),

            "facebook": self.facebook.search(query)

        }