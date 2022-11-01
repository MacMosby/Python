import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/e491fef3eb4d5e6ed8d5ef0a0905f6c5/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.data = requests.get(url=SHEETY_ENDPOINT).json()["prices"]

    def get_destination_data(self):
        return self.data

    def update_destination_codes(self, sheet_data):
        for airport in sheet_data:
            params = {
                "price": {
                    "city": airport["city"],
                    "iataCode": airport["iataCode"],
                    "lowestPrice": airport["lowestPrice"]
                }
            }

            requests.put(url=f"{SHEETY_ENDPOINT}/{airport['id']}", json=params)



