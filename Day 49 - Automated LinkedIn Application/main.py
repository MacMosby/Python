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

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_WT=2&keywords=Python%20Developer&location=Weltweit&sortBy=R")
driver.maximize_window()

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(3)

username_input = driver.find_element(By.ID, "username")
# username_input.click()
username_input.send_keys("put your email here")
pw_input = driver.find_element(By.ID, "password")
pw_input.send_keys("put your linkedin password here")
pw_input.send_keys(Keys.ENTER)

time.sleep(10)

jobs = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results-list ul .job-card-container--clickable")


for job in jobs:
    job.click()
    time.sleep(3)
    save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    save_button.click()
    time.sleep(3)
    close = driver.find_element(By.CSS_SELECTOR, ".artdeco-toast-item--visible button path")
    close.click()
    time.sleep(1)

driver.quit()
