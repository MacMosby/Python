import requests
from datetime import datetime, timedelta
from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_destination_code(self, city_name):

        config = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "city",
            "active_only": "true"
        }

        header = {
            "apikey": "put your api key here"
        }

        response = requests.get(url="https://api.tequila.kiwi.com/locations/query",
                                params=config,
                                headers=header)
        code = response.json()["locations"][0]["code"]
        return code

    def search_flight(self, code, stopovers):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        end_of_search = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        header = {
            "apikey": "put your api key here",
            "accept": "application/json"
        }
        response = requests.get(
            url=f"https://api.tequila.kiwi.com/v2/search?fly_from=LON&fly_to={code}&date_from={tomorrow}&date_to={end_of_search}&one_for_city=1&curr=GBP&max_stopovers={stopovers}&nights_in_destination_from=2&nights_in_destination_to=28",
            headers=header
        )

        response.raise_for_status()
        flight = FlightData()
        flight.arrival_airport_code = code
        try:
            flight.departure_city = response.json()["data"][0]["cityFrom"]
            flight.price = response.json()["data"][0]["conversion"]["GBP"]
            flight.arrival_city = response.json()["data"][0]["cityTo"]
            flight.departure_airport_code = response.json()["data"][0]["flyFrom"]
            departure = (response.json()["data"][0]["route"][0]["local_departure"]).split("T")
            flight.outbound_date = departure[0]
            arrival = (response.json()["data"][0]["route"][0]["local_arrival"]).split("T")
            flight.inbound_date = arrival[0]
            print(f"{flight.arrival_city}: GBP{flight.price}")
        except IndexError:
            print(f"No flight found for {code}")
        else:
            return flight
