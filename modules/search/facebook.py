from urllib.parse import quote

from playwright.sync_api import sync_playwright


class FacebookSearch:

    def search(self, query):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page()

            url = (
                "https://www.facebook.com/marketplace/search/"
                f"?query={quote(query)}"
            )

            try:

                page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=30000
                )

                page.wait_for_timeout(5000)

                products = []

                cards = page.locator("a[href*='/marketplace/item/']")

                count = cards.count()

                seen = set()

                for i in range(min(count, 10)):

                    card = cards.nth(i)

                    try:
                        href = card.get_attribute("href")
                    except:
                        continue

                    if not href:
                        continue

                    if href.startswith("/"):
                        href = "https://www.facebook.com" + href

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

                return {

                    "platform": "Facebook",

                    "found": len(products) > 0,

                    "count": len(products),

                    "products": products

                }

            except:

                browser.close()

                return {

                    "platform": "Facebook",

                    "found": False,

                    "count": 0,

                    "products": []

                }