import requests
from datetime import datetime

from app.config import (
    SHEETY_ENDPOINT,
    SHEETY_USERNAME,
    SHEETY_PASSWORD,
)


now = datetime.now()

data = {
    "sheet1": {
        "date": now.strftime("%d/%m/%Y"),
        "time": now.strftime("%H:%M:%S"),
        "exercise": "Jumping",
        "duration": 30,
        "calories": 176,
    }
}

response = requests.post(
    SHEETY_ENDPOINT,
    json=data,
    headers={
        "Content-Type": "application/json"
    },
    auth=(
        SHEETY_USERNAME,
        SHEETY_PASSWORD,
    ),
    timeout=30,
)

print("Status:", response.status_code)
print("Response:", response.text)