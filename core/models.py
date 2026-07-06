from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class VisionResult:

    product_name: str

    category: str

    keywords: List[str]

    confidence: float

    success: bool = True


@dataclass
class ProductResult:

    title: str

    price: str = ""

    url: str = ""

    image: str = ""

    rating: str = ""

    reviews: str = ""


@dataclass
class SearchResult:

    platform: str

    found: bool

    count: int

    products: List[Dict] = field(default_factory=list)

    links: List[str] = field(default_factory=list)

    videos: List[Dict] = field(default_factory=list)