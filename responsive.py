import time
from math import ceil
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ResponsiveTester:
    def __init__(self, urls):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.urls = urls
        self.sizes = [320, 480, 960, 1366, 1920]

    def screenshot(self, url):
        BROWSER_HEIGHT = 1027
        self.browser.get(url)

        for size in self.sizes:
            self.browser.set_window_size(size, BROWSER_HEIGHT)
            self.browser.execute_script("window.scrollTo(0, 0)")
            time.sleep(2)
            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight")
            total_sections = ceil(scroll_size / BROWSER_HEIGHT)
            for section in range(total_sections + 1):
                print(section, size)
                self.browser.execute_script(
                    f"window.scrollTo(0, {section * BROWSER_HEIGHT})")
                time.sleep(1)

                url = url.replace("https://", "")
                if not os.path.exists(f"screenshots/{url}/"):
                    os.makedirs(f"screenshots/{url}/")

                self.browser.save_screenshot(
                    f"screenshots/{url}/{size}x{section}.png")

    def start(self):
        for url in self.urls:
            self.screenshot(url)

    def quit(self):
        self.browser.quit()


tester = ResponsiveTester(["https://naver.com", "https://google.com"])
tester.start()
tester.quit()