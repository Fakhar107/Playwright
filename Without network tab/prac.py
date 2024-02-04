from playwright.sync_api import sync_playwright
import json

def test_json(response,results):
    try:
        results.append(
            {
                'url': response.url,
                'data': response.json(),
            }
        )
    except:
        pass

def run(playwright):
    results = []
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)# to get results make it headed.
    page = browser.new_page()
    
    page.on('response',lambda response: test_json(response, results))
    page.goto('https://adidas.com/terrex') # changed the site
    browser.close()
    return results

with sync_playwright() as playwright:
    data = run(playwright)
    with open('results.json', 'w') as f:
        json.dump(data,f)