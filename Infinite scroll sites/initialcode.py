from playwright.sync_api import sync_playwright
import time
from rich import print

def scroll_me():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size(
            {'width':1280, 'height': 1080}
        )
        page.goto('https://www.nike.com/gb/w/mens-shoes-nik1zy7ok')
        time.sleep(2)
        #page.click('#hf_cookie_text_cookieAccept')      
        page.wait_for_load_state('networkidle')
            # scrolldown
        for x in range(1,5):
            #page.keyboard.press('End')
            page.mouse.wheel(0,15000)
            print('scrolling key press',x)
        time.sleep(1)

    browser.close()

def main():
    scroll_me()

if __name__=='__main__':
    main()

