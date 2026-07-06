import hashlib
import json
from pathlib import Path


class Cache:

    def __init__(self):

        self.cache_dir = Path("cache")

        self.cache_dir.mkdir(exist_ok=True)

    def _hash(self, value):

        return hashlib.md5(

            value.encode()

        ).hexdigest()

    def exists(self, key):

        return (

            self.cache_dir /

            f"{self._hash(key)}.json"

        ).exists()

    def load(self, key):

        path = self.cache_dir / f"{self._hash(key)}.json"

        if not path.exists():

            return None

        with open(path, "r", encoding="utf-8") as f:

            return json.load(f)

    def save(self, key, data):

        path = self.cache_dir / f"{self._hash(key)}.json"

        with open(path, "w", encoding="utf-8") as f:

            json.dump(

                data,

                f,

                ensure_ascii=False,

                indent=4

            )