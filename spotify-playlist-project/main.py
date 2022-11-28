import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# --------------------------SPOTIFY API----------------------------------

auth_manager = SpotifyOAuth(
    client_id="use your client id",
    client_secret="use your client secret",
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    cache_path="token.txt",
    )

sp = spotipy.Spotify(auth_manager=auth_manager)

user_id = sp.current_user()["id"]
# print(user_id)

# --------------------------GET BILLBOARD CHARTS----------------------------------

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
charts_web_page = response.text

soup = BeautifulSoup(charts_web_page, "html.parser")
song_titles = soup.select("div .o-chart-results-list-row-container")

song_uris = []
for title_tag in song_titles:
    title = title_tag.select_one("h3")
    song = title.text.strip()
    result = sp.search(q=song, type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify.")


playlist = sp.user_playlist_create(user=user_id, name="Noice!", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)




