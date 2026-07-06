from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_FOLDER = BASE_DIR / "uploads"

VISION_MODEL = "gemma3:4b"

OLLAMA_URL = "http://localhost:11434/api/generate"

SEARCH_TIMEOUT = 30

HEADLESS = True

MAX_RESULTS = 10

USER_AGENT = (
    "Mozilla/5.0 "
    "(Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/137.0 Safari/537.36"
)