from modules.vision.engine import VisionEngine
from core.search_engine import SearchEngine


class AIHunterEngine:

    def __init__(self):

        self.vision = VisionEngine()

        self.search = SearchEngine()

    def analyze(self, image_path):

        vision = self.vision.detect(image_path)

        if not vision["success"]:
            return vision

        query = vision["keywords"][0]

        competition = self.search.search(query)

        return {

            "vision": vision,

            "competition": competition

        }