from urllib.parse import quote

from playwright.sync_api import sync_playwright

from core.base_search import BaseSearch


class TikTokSearch(BaseSearch):

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

                    f"https://www.tiktok.com/search?q={quote(query)}",

                    wait_until="domcontentloaded",

                    timeout=self.timeout * 1000

                )

                page.wait_for_timeout(5000)

                videos = []

                cards = page.locator("div[data-e2e='search_top-item']")

                count = min(

                    cards.count(),

                    self.max_results

                )

                for i in range(count):

                    card = cards.nth(i)

                    try:
                        title = card.inner_text()
                    except:
                        title = ""

                    try:
                        link = card.locator("a").first.get_attribute("href")

                        if link and link.startswith("/"):
                            link = "https://www.tiktok.com" + link

                    except:
                        link = ""

                    videos.append({

                        "title": title,

                        "url": link

                    })

                browser.close()

                return self.success(

                    "TikTok",

                    videos=videos

                )

        except Exception as e:

            return self.failed(

                "TikTok",

                e

            )