from abc import ABC, abstractmethod

from core.logger import logger
from core.config import (
    HEADLESS,
    MAX_RESULTS,
    SEARCH_TIMEOUT,
)


class BaseSearch(ABC):

    def __init__(self):

        self.headless = HEADLESS

        self.timeout = SEARCH_TIMEOUT

        self.max_results = MAX_RESULTS

    @abstractmethod
    def search(self, query):
        pass

    def success(self, platform, products=None, links=None, videos=None):

        products = products or []

        links = links or []

        videos = videos or []

        return {

            "platform": platform,

            "found": (
                len(products) > 0
                or len(links) > 0
                or len(videos) > 0
            ),

            "count": max(

                len(products),

                len(links),

                len(videos)

            ),

            "products": products,

            "links": links,

            "videos": videos

        }

    def failed(self, platform, error):

        logger.error(f"{platform}: {error}")

        return {

            "platform": platform,

            "found": False,

            "count": 0,

            "products": [],

            "links": [],

            "videos": [],

            "error": str(error)

        }