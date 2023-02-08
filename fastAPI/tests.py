import main
from main import Order
import unittest


class TestDeliveryFee(unittest.TestCase):

    def test_with_high_cart_value(self):
        self.assertEqual(main.calculate_delivery_fee(Order(cart_value=12000, delivery_distance=0, number_of_items=4, time="2023-02-09T13:00:00")),
            {"delivery_fee": 0})

    def test_with_low_cart_value_no_distance_few_items_outside_rush(self):
        self.assertEqual(main.calculate_delivery_fee(Order(cart_value=780, delivery_distance=0, number_of_items=4, time="2023-02-09T13:00:00Z")),
            {"delivery_fee": 420})

    def test_with_middle_cart_value_no_distance_few_items_outside_rush(self):
        self.assertEqual(main.calculate_delivery_fee(Order(cart_value=1000, delivery_distance=0, number_of_items=4, time="2023-02-09T13:00:00Z")),
            {"delivery_fee": 200})

    def test_with_middle_cart_value_short_distance_few_items_outside_rush(self):
        self.assertEqual(main.calculate_delivery_fee(Order(cart_value=1000, delivery_distance=999, number_of_items=4, time="2023-02-09T13:00:00Z")),
            {"delivery_fee": 200})

    def test_with_middle_cart_value_middle_distance_few_items_outside_rush(self):
        self.assertEqual(main.calculate_delivery_fee(Order(cart_value=1000, delivery_distance=1499, number_of_items=4, time="2023-02-09T13:00:00Z")),
            {"delivery_fee": 300})

    def test_with_middle_cart_value_middle_but_little_longer_distance_few_items_outside_rush(self):
        self.assertEqual(main.calculate_delivery_fee(Order(cart_value=1000, delivery_distance=1500, number_of_items=4, time="2023-02-09T13:00:00Z")),
            {"delivery_fee": 300})

    def test_with_middle_cart_value_middle_but_even_little_longer_distance_few_items_outside_rush(self):
        self.assertEqual(main.calculate_delivery_fee(Order(cart_value=1000, delivery_distance=1501, number_of_items=4, time="2023-02-09T13:00:00Z")),
            {"delivery_fee": 400})

    def test_with_middle_cart_value_long_distance_few_items_outside_rush(self):
        self.assertEqual(main.calculate_delivery_fee(Order(cart_value=1000, delivery_distance=15500000, number_of_items=4, time="2023-02-09T13:00:00Z")),
            {"delivery_fee": 1500})

    def test_with_middle_cart_value_no_distance_more_than_four_items_outside_rush(self):
        self.assertEqual(main.calculate_delivery_fee(Order(cart_value=1000, delivery_distance=0, number_of_items=6, time="2023-02-09T13:00:00Z")),
            {"delivery_fee": 300})

    def test_with_middle_cart_value_no_distance_more_than_twelve_items_outside_rush(self):
        self.assertEqual(main.calculate_delivery_fee(Order(cart_value=1000, delivery_distance=0, number_of_items=13, time="2023-02-09T13:00:00Z")),
            {"delivery_fee": 770})

    def test_with_middle_cart_value_no_distance_few_items_inside_rush(self):
        self.assertEqual(main.calculate_delivery_fee(Order(cart_value=1000, delivery_distance=0, number_of_items=4, time="2023-02-10T16:00:00Z")),
            {"delivery_fee": 240})








