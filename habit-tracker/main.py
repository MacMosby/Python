import requests
from datetime import datetime

USERNAME = "use your own user name"
TOKEN = "use your own token"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Running",
    "unit": "km",
    "type": "float",
    "color": "sora"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

today = datetime.now().strftime("%Y%m%d")
pixel_config = {
    "date": today,
    "quantity": input("How many km did you run today?")
}
response = requests.post(url=f"{graph_endpoint}/graph1", json=pixel_config, headers=header)
print(response.text)
