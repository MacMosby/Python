import requests

data = {"cart_value": 790,
                   "delivery_distance": 2235,
                   "number_of_items": 4,
                   "time": "2021-10-12T13:00:00Z"}

response = requests.post("http://127.0.0.1:8000/v1/delivery_fee", json=data)
print(response.status_code)
