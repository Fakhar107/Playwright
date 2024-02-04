from playwright.sync_api import sync_playwright

def test_json(response):
    try:
        print(response.json())
    except:
        pass


def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    
    page.on('response',lambda response: test_json(response))# In the step-1, all the json responses with errors etc came up 
    # but using this try except test_json will keep the execution of code moving despite issues.
    page.goto('https://www.nba.com/stats/players')
    browser.close()


with sync_playwright() as playwright:
    run(playwright)