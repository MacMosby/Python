import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
charts_web_page = response.text

soup = BeautifulSoup(charts_web_page, "html.parser")
song_titles = soup.select("div .o-chart-results-list-row-container")

for title_tag in song_titles:
    title = title_tag.select_one("h3")
    print(title.text.strip())



#--------------------------SPOTIFY API----------------------------------
