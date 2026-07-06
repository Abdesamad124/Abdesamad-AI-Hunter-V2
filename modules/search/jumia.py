from urllib.parse import quote

from playwright.sync_api import sync_playwright

from core.base_search import BaseSearch


class JumiaSearch(BaseSearch):

    def __init__(self):

        super().__init__()

    def search(self, query):

        try:

            with sync_playwright() as p:

                browser = p.chromium.launch(

                    headless=self.headless

                )

                page = browser.new_page()

                page.goto(

                    f"https://www.jumia.ma/catalog/?q={quote(query)}",

                    wait_until="domcontentloaded",

                    timeout=self.timeout * 1000

                )

                page.wait_for_timeout(4000)

                products = []

                cards = page.locator("article.prd")

                count = min(

                    cards.count(),

                    self.max_results

                )

                for i in range(count):

                    card = cards.nth(i)

                    try:
                        title = card.locator("h3.name").inner_text()
                    except:
                        title = ""

                    try:
                        price = card.locator(".prc").inner_text()
                    except:
                        price = ""

                    try:
                        link = card.locator("a.core").get_attribute("href")

                        if link and not link.startswith("http"):

                            link = "https://www.jumia.ma" + link

                    except:

                        link = ""

                    try:
                        image = card.locator("img").get_attribute("data-src")

                        if not image:

                            image = card.locator("img").get_attribute("src")

                    except:

                        image = ""

                    try:
                        rating = card.locator(".stars").get_attribute("aria-label") or ""

                    except:

                        rating = ""

                    try:
                        reviews = card.locator(".rev").inner_text()

                    except:

                        reviews = ""

                    products.append({

                        "title": title,

                        "price": price,

                        "url": link,

                        "image": image,

                        "rating": rating,

                        "reviews": reviews

                    })

                browser.close()

                return self.success(

                    "Jumia",

                    products=products

                )

        except Exception as e:

            return self.failed(

                "Jumia",

                e

            )