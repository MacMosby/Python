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

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
# cursor = driver.find_element(By.ID, "buyCursor")
# grandma = driver.find_element(By.ID, "buyGrandma")
# factory = driver.find_element(By.ID, "buyFactory")
# mine = driver.find_element(By.ID, "buyMine")
# shipment = driver.find_element(By.ID, "buyShipment")
# alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
# portal = driver.find_element(By.ID, "buyPortal")
# time_machine = driver.find_element(By.ID, "buyTime machine")

timeout = time.time() + 5
five_min = time.time() + 60*5

running = True

while running:
    cookie.click()

    if time.time() > timeout:

        # Get money count
        cookie_count = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        buttons = driver.find_elements(By.CSS_SELECTOR, "#store div")
        for button in reversed(buttons):
            element = button.text.split("-")
            if len(element) > 1:
                num = element[1].split("\n")[0].strip()
                cost = num.replace(",", "")
                if cookie_count > int(cost):
                    button.click()
                    break

        # Set time for next timeout
        timeout = time.time() + 5

    if time.time() > five_min:
        print(driver.find_element(By.ID, "cps").text)
        running = False

driver.quit()
