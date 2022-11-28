import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

header = {
    "User-Agent": "put your info here",
    "Accept-Language": "put your info here",
}
response = requests.get("https://www.amazon.de/Withings-Nokia-Body-WLAN-K%C3%B6rperwaage-K%C3%B6rperzusammensetzung/dp/B071XW4C5Q/", headers=header)
product_page = response.text

soup = BeautifulSoup(product_page, "lxml")
price_whole = soup.select_one(".a-price-whole").text.strip(",")
price_fraction = soup.select_one(".a-price-fraction").text
price = float(f"{price_whole}.{price_fraction}")
print(price)

if price < 80:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="put your gmail here", password="put your password here")
        connection.sendmail(
            from_addr="put your gmail here",
            to_addrs="put your gmail here",
            msg=f"Subject:Price Alert\n\nThe price is below 80€. Go buy now: https://www.amazon.de/Withings-Nokia-Body-WLAN-K%C3%B6rperwaage-K%C3%B6rperzusammensetzung/dp/B071XW4C5Q/"
        )

