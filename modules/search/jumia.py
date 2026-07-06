from urllib.parse import quote

from playwright.sync_api import sync_playwright


class JumiaSearch:

    def search(self, query):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page()

            url = f"https://www.jumia.ma/catalog/?q={quote(query)}"

            page.goto(
                url,
                wait_until="domcontentloaded"
            )

            page.wait_for_timeout(5000)

            products = []

            cards = page.locator("article.prd")

            count = cards.count()

            for i in range(min(count, 10)):

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

                    if not link:
                        link = card.locator("a").first.get_attribute("href")

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
                    rating = card.locator(".stars").get_attribute("aria-label")

                    if rating is None:
                        rating = ""

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

            return {

                "platform": "Jumia",

                "found": len(products) > 0,

                "count": len(products),

                "products": products

            }