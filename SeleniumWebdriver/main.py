from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/marcrodenbusch/code/chromedriver"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
driver.get("https://www.python.org")


nav_bar = driver.find_element(by="By.ID", value="top")
print(nav_bar)

driver.quit()
