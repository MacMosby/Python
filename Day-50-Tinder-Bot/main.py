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
driver.maximize_window()

time.sleep(3)

accept_button = driver.find_element(By.XPATH, '//*[@id="q1392377819"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_button.click()

time.sleep(3)

log_in_button = driver.find_element(By.LINK_TEXT, "Log in")
log_in_button.click()

time.sleep(3)

facebook = driver.find_element(By.XPATH, '//*[@id="q1613718255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook.click()

time.sleep(1)

fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)

time.sleep(1)

cookies = driver.find_elements(By.CSS_SELECTOR, "button")[5]
cookies.click()

time.sleep(1)

mail = driver.find_element(By.ID, "email")
mail.send_keys("marcrodenbusch@gmail.com")
pw = driver.find_element(By.ID, "pass")
pw.send_keys("A4c6YG7BW=%UvS/")
pw.send_keys(Keys.ENTER)

time.sleep(10)

tinder = driver.window_handles[0]
driver.switch_to.window(tinder)

location = driver.find_element(By.XPATH, '//*[@id="q1613718255"]/main/div/div/div/div[3]/button[1]')
location.click()

time.sleep(2)

notifications = driver.find_element(By.XPATH, '//*[@id="q1613718255"]/main/div/div/div/div[3]/button[1]')
notifications.click()

time.sleep(6)

no_dark_mode = driver.find_element(By.XPATH, '//*[@id="q1613718255"]/main/div/div[2]/button')
no_dark_mode.click()

time.sleep(2)

likes_received = driver.find_element(By.XPATH, '//*[@id="q1613718255"]/main/div/div/div[3]/button[2]')
likes_received.click()

time.sleep(2)

# profile = driver.find_element(By.XPATH, '//*[@id="q1392377819"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/button')
# profile.click()
time.sleep(2)
like = driver.find_element(By.XPATH, '//*[@id="q1392377819"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
like.click()
