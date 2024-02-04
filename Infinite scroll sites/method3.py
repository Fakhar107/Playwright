from playwright.sync_api import sync_playwright
import time
from rich import print

def scroll_me():
    def check_json(response):
        if 'products' in response.url:
            print({'url': response.url, 'body': response.json})
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size(
            {'width':1280, 'height': 1080}
        )
        page.on('response', lambda response: check_json(response))# newtwork responses
        page.goto('https://www.nike.com/gb/w/mens-shoes-nik1zy7ok')
        time.sleep(2)
        #page.click('#hf_cookie_text_cookieAccept') #if there is a cookie
        element_selector =  'div.banner-subtitle.css-1epojjp'    
        page.wait_for_selector(element_selector, timeout=60000)
        for x in range(1,5):
            page.evaluate('window.scrollTo(0, document.body.scrollHeight);')
            print('scrolling key press',x)
        time.sleep(1)

        browser.close()

def main():
    scroll_me()

if __name__=='__main__':
    main()


