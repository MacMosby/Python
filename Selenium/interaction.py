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
cursor = driver.find_element(By.ID, "buyCursor")
grandma = driver.find_element(By.ID, "buyGrandma")
factory = driver.find_element(By.ID, "buyFactory")
mine = driver.find_element(By.ID, "buyMine")
shipment = driver.find_element(By.ID, "buyShipment")
alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
portal = driver.find_element(By.ID, "buyPortal")
time_machine = driver.find_element(By.ID, "buyTime machine")

while True:
    for _ in range(1000):
        cookie.click()
    if time_machine.get_attribute("class") != "grayed":
        time_machine.click()
    else:
        if portal.get_attribute("class") != "grayed":
            portal.click()
        else:
            if alchemy_lab.get_attribute("class") != "grayed":
                alchemy_lab.click()
            else:
                if shipment.get_attribute("class") != "grayed":
                    shipment.click()
                else:
                    if mine.get_attribute("class") != "grayed":
                        mine.click()
                    else:
                        if factory.get_attribute("class") != "grayed":
                            factory.click()
                        else:
                            if grandma.get_attribute("class") != "grayed":
                                grandma.click()
                            else:
                                if cursor.get_attribute("class") != "grayed":
                                    cursor.click()
    time.sleep(5)


