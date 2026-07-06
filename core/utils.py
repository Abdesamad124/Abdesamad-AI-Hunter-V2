import os
import uuid
from pathlib import Path


def generate_filename(filename: str):

    extension = Path(filename).suffix

    return f"{uuid.uuid4().hex}{extension}"


def ensure_folder(folder):

    os.makedirs(folder, exist_ok=True)


def safe_get(dictionary, key, default=None):

    try:
        return dictionary[key]
    except Exception:
        return default