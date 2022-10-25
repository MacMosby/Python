import requests
import os

pixela_endpoint = "https://pixe.la/v1/users"
token = os.environ["PIXELA_USER_TOKEN"]

user_parameters = {
    "token": "token",
    "username": "MacMosby",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_parameters)
print(response.text)

os.environ