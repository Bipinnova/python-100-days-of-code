import requests

PIXELA_USERNAME = "bipin-habit-tracker"
PIXELA_TOKEN = "rUxUGa0-3eglQnR5QSw2jCPbFmjXTu8dCFoZdmLl-34"

BASE_URL = "https://pixe.la/v1/users"

GRAPH_IDS = [
    "test-graph",
    "u1-daily-reading",
    "u4-coding-world",
]

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}


for graph_id in GRAPH_IDS:

    url = (
        f"{BASE_URL}/"
        f"{PIXELA_USERNAME}/graphs/"
        f"{graph_id}"
    )

    response = requests.delete(
        url,
        headers=headers,
        timeout=10
    )

    print(f"\nGraph: {graph_id}")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")