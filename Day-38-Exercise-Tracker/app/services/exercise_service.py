import requests

from app.config import (
    NIX_APP_ID,
    NIX_API_KEY,
    GENDER,
    WEIGHT_KG,
    HEIGHT_CM,
    AGE,
)


EXERCISE_ENDPOINT = (
    "https://app.100daysofpython.dev/"
    "v1/nutrition/natural/exercise"
)


def get_exercises(exercise_text: str):

    headers = {
        "x-app-id": NIX_APP_ID,
        "x-app-key": NIX_API_KEY,
    }

    parameters = {
        "query": exercise_text,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
    }

    response = requests.post(
        EXERCISE_ENDPOINT,
        json=parameters,
        headers=headers,
        timeout=30,
    )

    response.raise_for_status()

    result = response.json()

    if "error" in result:
        raise ValueError(
            result["error"].get("message", "Exercise API error")
        )

    return result["exercises"]