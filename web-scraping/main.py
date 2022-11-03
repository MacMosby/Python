import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_wep_page = response.text
soup = BeautifulSoup(movies_wep_page, "html.parser")

title_tags = soup.find_all(name="h3", class_="title")
title_tags.reverse()


with open("movies.txt", "w") as file:
    for tag in title_tags:
        file.write(f"{tag.text}\n")





















#----------------------------------------------------------------------------------------

# response = requests.get("https://news.ycombinator.com/")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
# articles = []
# article_tags = soup.select(selector=".titleline a")
# for n in range(len(article_tags)):
#     if n % 2 == 0:
#         articles.append(article_tags[n])
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.select(selector=".score")]
#
# article_texts = []
# article_links = []
#
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)
#
# print(article_texts)
# print(article_links)
# print(article_upvotes)
#
# index = article_upvotes.index(max(article_upvotes))
# print(article_texts[index])



#-------------------------------------------------------------------------------


# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# print(soup.title)
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(class_=)
# print(heading.string)
