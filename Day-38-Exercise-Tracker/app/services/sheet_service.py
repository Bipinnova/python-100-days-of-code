# import requests
# from datetime import datetime

# from app.config import (
#     SHEETY_ENDPOINT,
#     SHEETY_USERNAME,
#     SHEETY_PASSWORD,
# )


# def save_exercise(exercise: dict):

#     now = datetime.now()

#     sheet_data = {
#         "sheet1": {
#             "date": now.strftime("%d/%m/%Y"),
#             "time": now.strftime("%H:%M:%S"),
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"],
#         }
#     }

#     response = requests.post(
#         SHEETY_ENDPOINT,
#         json=sheet_data,
#         auth=(
#             SHEETY_USERNAME,
#             SHEETY_PASSWORD,
#         ),
#         timeout=30,
#     )

#     response.raise_for_status()

#     return response.json()

import requests
from datetime import datetime

from app.config import (
    SHEETY_ENDPOINT,
    SHEETY_USERNAME,
    SHEETY_PASSWORD,
)


def save_exercise(exercise: dict):

    now = datetime.now()

    sheet_data = {
        "sheet1": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post(
        SHEETY_ENDPOINT,
        json=sheet_data,
        headers=headers,
        auth=(
            SHEETY_USERNAME,
            SHEETY_PASSWORD,
        ),
        timeout=30,
    )

    if response.status_code not in (200, 201):
        raise RuntimeError(
            f"Sheety API error: "
            f"{response.status_code} - {response.text}"
        )

    return response.json()