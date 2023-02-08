from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from math import ceil

app = FastAPI()


class Order(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str
    delivery_fee: Optional[int]

    class Config:
        fields = {
            'time': {'format': '%Y-%m-%dT%H:%M:%SZ'}
        }


@app.post("/v1/fees")
def calculate_delivery_fee(order: Order):

    # # Validating the input types and format
    # if type(order.cart_value) is not int:
    #     raise TypeError("Cart value has invalid type.")
    # else:
    #     value = order.cart_value
    # if type(order.delivery_distance) is not int:
    #     raise TypeError("Delivery distance has invalid type.")
    # else:
    #     distance = order.delivery_distance
    # if type(order.number_of_items) is not int:
    #     raise TypeError("Number of items has invalid type.")
    # else:
    #     items = order.number_of_items
    # if type(order.time) is not str:
    #     raise TypeError("Time has invalid type.")
    # else:
    #     if bool(datetime.strptime(order.time, '%Y-%m-%dT%H:%M:%SZ')):
    #         time = datetime.strptime(order.time, '%Y-%m-%dT%H:%M:%SZ')
    #     else:
    #         raise ValueError("Time has not the right format.")
    value = order.cart_value
    distance = order.delivery_distance
    items = order.number_of_items
    time = datetime.strptime(order.time, '%Y-%m-%dT%H:%M:%SZ')
    fee = 0

    # Set fee to 0 if cart value 100€ or more
    if value >= 10000:
        fee = 0
    else:
        # Add fee if order is smaller than 10€
        if value < 1000:
            fee += 1000 - value
        # Add 2€ for the first km and lower the distance by 1000 (first km)
        fee += 200
        distance -= 1000
        # Add additional distance fee
        if distance > 0:
            fee += ceil(distance / 500) * 100
        # Add additional fee for surplus of item (more than 4)
        if items > 4:
            items_surplus = items - 4
            fee += items_surplus * 50
            if items > 12:
                fee += 120
        # Add fee multiplication factor based on time
        rush_start = datetime.strptime("15:00:00", "%H:%M:%S").time()
        rush_end = datetime.strptime("19:00:00", "%H:%M:%S").time()
        if time.date().weekday() == 4 and rush_start <= time.time() <= rush_end:
            fee *= 1.2
        # Set maximum fee
        if fee > 1500:
            fee = 1500

    order.delivery_fee = fee
    return {"delivery_fee": order.delivery_fee}
