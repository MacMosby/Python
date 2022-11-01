import requests

print("Welcome to Marc's Flight Club\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email1 = input("What is your email?\n")
email2 = input("What is your email?\n")
if email1 == email2:
    print("You're in the club!")
    user = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email1
        }
    }
    response = requests.post(url="https://api.sheety.co/e491fef3eb4d5e6ed8d5ef0a0905f6c5/flightDeals/users", json=user)
    response.raise_for_status()
    print(response.text)