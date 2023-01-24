import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/marcrodenbusch/code/chromedriver"
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.tinder.com")
# driver.maximize_window()

time.sleep(10)

log_in_button = driver.find_element(By.LINK_TEXT, "Log in")
log_in_button.click()

time.sleep(5)

facebook = driver.find_element(By.LINK_TEXT, "Login with Facebook")
facebook.click()
