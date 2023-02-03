from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class Order(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str
    delivery_fee: int


# @app.get("/")
# def root():
#     pass


@app.post("/v1/delivery_fee")
def calculate_delivery_fee(order: Order):
    value = order.cart_value
    distance = order.delivery_distance
    items = order.number_of_items
    time = order.time
    fee = 0

    # Add fee if order is smaller than 10€
    if value < 1000:
        fee += 1000 - value
    # Add 2€ for the first km
    fee += 200
    # Add additional distance fee
    if distance > 1000:
        distance -= 1000
        additional_distance_fee = (((distance - 1) / 500) + 1) * 100
        fee += additional_distance_fee
    # Add additional fee for surplus of item (more than 4)
    if items > 4:
        items_surplus = items - 4
        fee += items_surplus * 50
        if items > 12:
            fee += 120
    # Add fee multiplication factor based on time
    if time # = rush hour:
        pass
    # Set maximum fee
    if fee > 1500:
        fee = 1500
    # Set fee to 0 if cart value 100€ or more
    if value >= 10000:
        fee = 0
    order.delivery_fee = fee

    return {"delivery_fee": order.delivery_fee}
