from modules.vision.engine import VisionEngine
from core.search_engine import SearchEngine
from core.cache import Cache
from core.image_hash import ImageHash


class AIHunterEngine:

    def __init__(self):

        self.vision = VisionEngine()

        self.search = SearchEngine()

        self.cache = Cache()

    def analyze(self, image_path):

        image_key = ImageHash.generate(image_path)

        if self.cache.exists(image_key):

            return self.cache.load(image_key)

        vision = self.vision.detect(image_path)

        if not vision["success"]:

            return vision

        query = vision["keywords"][0]

        competition = self.search.search(query)

        result = {

            "vision": vision,

            "competition": competition

        }

        self.cache.save(

            image_key,

            result

        )

        return result