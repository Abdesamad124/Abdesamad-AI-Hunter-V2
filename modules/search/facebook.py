from urllib.parse import quote

from playwright.sync_api import sync_playwright

from core.base_search import BaseSearch


class FacebookSearch(BaseSearch):

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

                    f"https://www.facebook.com/marketplace/search/?query={quote(query)}",

                    wait_until="domcontentloaded",

                    timeout=self.timeout * 1000

                )

                page.wait_for_timeout(5000)

                products = []

                cards = page.locator(

                    "a[href*='/marketplace/item/']"

                )

                count = min(

                    cards.count(),

                    self.max_results

                )

                seen = set()

                for i in range(count):

                    card = cards.nth(i)

                    try:

                        href = card.get_attribute("href")

                        if not href:

                            continue

                        if href.startswith("/"):

                            href = "https://www.facebook.com" + href

                    except:

                        continue

                    if href in seen:

                        continue

                    seen.add(href)

                    try:

                        title = card.inner_text().split("\n")[0]

                    except:

                        title = ""

                    products.append({

                        "title": title,

                        "url": href

                    })

                browser.close()

                return self.success(

                    "Facebook",

                    products=products

                )

        except Exception as e:

            return self.failed(

                "Facebook",

                e

            )