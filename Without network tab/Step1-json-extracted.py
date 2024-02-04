from playwright.sync_api import sync_playwright


def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    # Subscribe to 'request' and 'response' events.
    page.on('request',lambda request:print('>>', request.method, request.url))
    page.on('response',lambda response:print('<<', response.status, response.json))
    page.goto('https://www.nba.com/stats/players')
    browser.close()


with sync_playwright() as playwright:
    run(playwright)