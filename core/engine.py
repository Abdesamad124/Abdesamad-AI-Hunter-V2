from modules.vision.engine import VisionEngine
from core.search_engine import SearchEngine
from core.cache import Cache
from core.image_hash import ImageHash
from core.report import Report
from core.morocco_detector import MoroccoDetector


class AIHunterEngine:

    def __init__(self):

        self.vision = VisionEngine()

        self.search = SearchEngine()

        self.cache = Cache()

    def analyze(self, image_path):

        key = ImageHash.generate(image_path)

        if self.cache.exists(key):

            return self.cache.load(key)

        vision = self.vision.detect(image_path)

        if not vision["success"]:

            return vision

        query = vision["keywords"][0]

        competition = self.search.search(query)

        report = Report.generate(
            vision,
            competition
        )

        morocco = MoroccoDetector.detect(
            competition
        )

        result = {

            "vision": vision,

            "competition": competition,

            "report": report,

            "morocco": morocco

        }

        self.cache.save(
            key,
            result
        )

        return result