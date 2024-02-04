# How To Scrape (almost) ANY Website with Python
# https://www.youtube.com/watch?v=A9ZDqxvwNDs

from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser

def parse_item(html_page):
    results = []
    html = HTMLParser(html_page)
    data = html.css("div.caption")
    for item in data:
        product = {
                'title' : item.css_first('a.title').attributes['title'],
                'price' : item.css_first('h4.pull-right.price').text()
                }
        results.append(product)
    return results

def main():
    url = 'https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops'
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url,wait_until='networkidle')
        next_page = page.locator('.next')
        while True:
            print(parse_item(page.content()))
            if next_page.is_disabled():
                break
            page.click('.next')
            page.wait_for_load_state('networkidle')
if __name__=='__main__':
    main()












    