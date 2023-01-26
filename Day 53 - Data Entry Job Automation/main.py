import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# PART OF BEAUTIFUL SOUP

# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
#
# response = requests.get(URL)
# movies_wep_page = response.text
# soup = BeautifulSoup(movies_wep_page, "html.parser")
#
# title_tags = soup.find_all(name="h3", class_="title")
# title_tags.reverse()
#
#
# with open("movies.txt", "w") as file:
#     for tag in title_tags:
#         file.write(f"{tag.text}\n")


# PART OF SELENIUM

# chrome_driver_path = "/Users/marcrodenbusch/code/chromedriver"
# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#
# driver.get("https://orteil.dashnet.org/experiments/cookie/")
# cookie = driver.find_element(By.ID, "cookie")
