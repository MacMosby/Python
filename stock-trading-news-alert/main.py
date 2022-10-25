import requests
import datetime as dt
import math
from twilio.rest import Client

TSLA_API_key = "use your own api key"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

parameters_tsla = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "compact",
    "apikey": TSLA_API_key
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters_tsla)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (day, value) in data.items()]
value_yesterday = float(data_list[0]["4. close"])
value_day_bf_yesterday = float(data_list[1]["4. close"])

change = value_yesterday/value_day_bf_yesterday * 100
trend = ""
percentage = math.floor(abs(100 - change))
if percentage >= 5:
    if change > 100:
        trend = f"🔺 {percentage}%"
    else:
        trend = f"🔻 {percentage}%"



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


    NEWS_API_KEY = "use your own api key"

    parameters_news = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }

    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters_news)
    response.raise_for_status()
    data = response.json()
    results = data["articles"][:3]

    message = f"TSLA {trend}"

    for article in results:
        message += "\nHeadline:"
        message += article["title"]
        message += "\nBrief"
        message += article["description"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

    account_sid = "use your own sid"
    auth_token = "use your own token"
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=message,
                         from_='set your twilio number',
                         to='set your own number'
                     )

    print(message.sid)


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

