import requests

from app.core.config import (
    PIXELA_BASE_URL,
    PIXELA_USERNAME,
    PIXELA_TOKEN,
)


def create_pixela_user():

    url = f"{PIXELA_BASE_URL}/users"

    payload = {
        "token": PIXELA_TOKEN,
        "username": PIXELA_USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(
        url,
        json=payload,
        timeout=10
    )

    print("Pixela status:", response.status_code)
    print("Pixela response:", response.text)


if __name__ == "__main__":
    create_pixela_user()