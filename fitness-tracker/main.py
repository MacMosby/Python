import requests
from datetime import datetime

APP_ID = "use your own app id"
API_KEY = "use your own api key"

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

workout = input("Tell me which exercises you did: ")

exercise_data = {
    "query": workout,
    "gender": "male",
    "weight_kg": 76.5,
    "height_cm": 188.00,
    "age": 33
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
              headers=header,
              json=exercise_data
              )
result = response.json()["exercises"]

for data in result:

    sheety_url = "https://api.sheety.co/e491fef3eb4d5e6ed8d5ef0a0905f6c5/workoutTracking/workouts"
    sheety_token = {
        "Authorization": "Bearer use your own bearer"
    }

    workout = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": data["name"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_url, json=workout, headers=sheety_token)
    print(sheet_response.text)
