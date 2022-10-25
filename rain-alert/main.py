import requests
from twilio.rest import Client

parameters = {
    "lat": 52.519665,
    "lon": 13.506570,
    "appid": "3497a602bcd90a3720da0a09da549a5a",
    "exclude": "current,minutely,daily"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()["hourly"]
print(data)

for hour in range(12):
    if int(data[hour]["weather"][0]["id"]) < 700:
        print("Bring umbrella.")
        break

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "put your id here"
auth_token = "put your auth code here"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="It's going to rain, bring an umbrella. ☔️",
                     from_="put your twilio number here",
                     to="put the recipient number here"
                 )

print(message.sid)
