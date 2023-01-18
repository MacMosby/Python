from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/marcrodenbusch/code/chromedriver"
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.python.org")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

events_dict = {}

for n in range(len(events)):
    event_info = events[n].text
    time = event_info.split("\n")[0]
    name = event_info.split("\n")[1]
    events_dict[n] = {
        "time": time,
        "name": name
    }

print(events_dict)










driver.quit()
