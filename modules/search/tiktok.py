from urllib.parse import quote

from playwright.sync_api import sync_playwright


class TikTokSearch:

    def search(self, query):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page()

            url = f"https://www.tiktok.com/search?q={quote(query)}"

            try:

                page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=30000
                )

                page.wait_for_timeout(5000)

                videos = []

                cards = page.locator("div[data-e2e='search_top-item']")

                count = cards.count()

                for i in range(min(count, 10)):

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

                return {

                    "platform": "TikTok",

                    "found": len(videos) > 0,

                    "count": len(videos),

                    "videos": videos

                }

            except:

                browser.close()

                return {

                    "platform": "TikTok",

                    "found": False,

                    "count": 0,

                    "videos": []

                }