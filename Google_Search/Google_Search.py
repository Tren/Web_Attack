from urllib.parse import urlparse

from playwright.sync_api import Playwright, sync_playwright

def search_and_save_urls(playwright: Playwright, num_results: int) -> None:
    query = "Python编程"
    google_url = f"https://www.google.com/search?q={query}&num={num_results}"

    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto(google_url)

    while True:
        page.wait_for_selector("#search")

        urls = page.query_selector_all(".yuRUbf > a")
        for url in urls:
            parsed_url = urlparse(url.get_attribute("href"))
            domain = parsed_url.netloc
            if domain not in domains:
                domains.add(domain)
                print(url.get_attribute("href"))

                with open("filtered_results.txt", "a", encoding="utf-8") as f:
                    f.write(url.get_attribute("href") + "\n")

        next_page_link = page.query_selector(".pn")
        if next_page_link is None:
            break

        next_page_link.click()

    browser.close()


with sync_playwright() as playwright:
    domains = set()
    search_and_save_urls(playwright, num_results=20000)
