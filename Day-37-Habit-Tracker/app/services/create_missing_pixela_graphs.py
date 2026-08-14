from app.core.config import (
    PIXELA_BASE_URL,
    PIXELA_USERNAME,
    PIXELA_TOKEN,
)

import requests


headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}


graphs = [
    {
        "id": "u4-coding-world",
        "name": "Coding World",
        "unit": "minutes",
        "type": "int",
        "color": "sora"
    },
    {
        "id": "u1-daily-reading",
        "name": "Daily Reading",
        "unit": "pages",
        "type": "int",
        "color": "ajisai"
    }
]


url = (
    f"{PIXELA_BASE_URL}/users/"
    f"{PIXELA_USERNAME}/graphs"
)


for graph in graphs:

    response = requests.post(
        url,
        json=graph,
        headers=headers,
        timeout=10
    )

    print("=" * 50)
    print("Graph:", graph["id"])
    print("Status:", response.status_code)
    print("Response:", response.text)