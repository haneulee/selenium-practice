from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://repl.it/login")

username_input = browser.find_element_by_xpath(
    "/html/body/div/div/div[3]/div[2]/div[1]/div[2]/form/div[1]/div/div/input")

password_input = browser.find_element_by_xpath(
    "/html/body/div/div/div[3]/div[2]/div[1]/div[2]/form/div[2]/div/div/div/input"
)

# login_btn = browser.find_element_by_partial_link_text("Log") #only look for a link tag
login_btn = browser.find_element_by_xpath(
    "/html/body/div/div/div[3]/div[2]/div[1]/div[2]/form/button")

# username_input.send_keys("haneulee")
# password_input.send_keys(input("what is your password?"))
# login_btn.click()

github_btn = browser.find_element_by_xpath(
    "/html/body/div/div/div[3]/div[2]/div[1]/div[1]/a[2]")
github_btn.click()
WebDriverWait(browser, 10).until(EC.url_changes("https://repl.it/~"))

title = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "username")))

print(title.text)
