from data_manager import DataManager
from flight_search import FlightSearch
from twilio.rest import Client

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()

print(sheet_data)

# for airport in sheet_data:
#     if airport["iataCode"] == "":
#         airport["iataCode"] = flight_search.get_destination_code(airport["city"])
#
# data_manager.update_destination_codes(sheet_data)

for row in sheet_data:
    flight = flight_search.search_flight(row["iataCode"], "0")
    if flight is None:
        flight_search.search_flight(row["iataCode"], "1")
    try:
        if flight.price < row["lowestPrice"]:
            account_sid = "put your account sid here"
            auth_token = "put your auth token here"
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body=f"Low price alert! Only GBP{flight.price} "
                        f"to fly from {flight.departure_city}-{flight.departure_airport_code} "
                        f"to {flight.arrival_city}-{flight.arrival_airport_code}, "
                        f"from {flight.outbound_date} to {flight.inbound_date}.",
                    from_='put your twilio number here',
                    to='put your phone number here'
                )

            print(message.status)
    except AttributeError:
        pass
