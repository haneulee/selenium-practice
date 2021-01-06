from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class GoogleKeywordScreenshooter():
    def __init__(self, keyword, screenshots_dir, max_pages):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        self.screenshots_dir = screenshots_dir
        self.max_pages = max_pages

    def start(self):
        self.browser.get("https://google.com")
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyword)
        search_bar.send_keys(Keys.ENTER)
        temp = self.max_pages

        while True:
            try:
                shitty_element = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "g-blk")))

                self.browser.execute_script(
                    """
                const shitty = arguments[0]
                shitty.parentElement.removeChild(shitty)
                """, shitty_element)
            except:
                pass

            search_results = self.browser.find_elements_by_class_name("g")

            for index, search_result in enumerate(search_results):
                search_result.screenshot(
                    f"{self.screenshots_dir}/page{temp}_{self.keyword}x{index}.png"
                )

            temp = temp - 1

            if temp == 0:
                break
            else:
                selected_page = self.browser.find_element_by_class_name(
                    "YyVfkd")
                next_sibling = self.browser.execute_script(
                    """
                    return arguments[0].nextElementSibling
                """, selected_page)
                next_sibling.click()

    def finish(self):
        self.browser.quit()


domain_competitors = GoogleKeywordScreenshooter("buy domain", "screenshots", 2)
domain_competitors.start()
domain_competitors.finish()
python_competitors = GoogleKeywordScreenshooter("python book", "screenshots",
                                                1)
python_competitors.start()
python_competitors.finish()

# browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# browser.quit()