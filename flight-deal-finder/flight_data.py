class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self):
        self.price = 0
        self.departure_airport_code = ""
        self.departure_city = ""
        self.arrival_airport_code = ""
        self.arrival_city = ""
        self.outbound_date = ""
        self.inbound_date = ""
        self.stop_overs = 0
        self.via_city = ""
