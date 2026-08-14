import requests

from app.core.config import (
    PIXELA_BASE_URL,
    PIXELA_TOKEN,
    PIXELA_USERNAME,
)


PIXELA_TYPE_MAP = {
    "whole_number": "int",
    "decimal": "float",
}


PIXELA_COLOR_MAP = {
    "green": "shibafu",
    "blue": "sora",
    "purple": "ajisai",
    "red": "momiji",
    "yellow": "ichou",
}


class PixelaService:

    def __init__(self):
        self.base_url = PIXELA_BASE_URL
        self.username = PIXELA_USERNAME
        self.token = PIXELA_TOKEN

        self.headers = {
            "X-USER-TOKEN": self.token
        }

    # --------------------------------------------------
    # Create Graph
    # --------------------------------------------------

    def create_graph(
        self,
        graph_id: str,
        name: str,
        unit: str,
        data_type: str,
        color: str
    ):

        url = (
            f"{self.base_url}/users/"
            f"{self.username}/graphs"
        )

        pixela_type = PIXELA_TYPE_MAP[data_type]
        pixela_color = PIXELA_COLOR_MAP[color]

        payload = {
            "id": graph_id,
            "name": name,
            "unit": unit,
            "type": pixela_type,
            "color": pixela_color
        }

        response = requests.post(
            url,
            json=payload,
            headers=self.headers,
            timeout=10
        )

        if not response.ok:
            print("Pixela status:", response.status_code)
            print("Pixela response:", response.text)
            raise Exception(
                f"Pixela graph creation failed: "
                f"{response.status_code} - {response.text}"
            )

        return response.json()

    # --------------------------------------------------
    # Create Pixel
    # --------------------------------------------------

    def create_pixel(
        self,
        graph_id: str,
        record_date: str,
        quantity: str
    ):

        url = (
            f"{self.base_url}/users/"
            f"{self.username}/graphs/"
            f"{graph_id}"
        )

        payload = {
            "date": record_date,
            "quantity": quantity
        }

        response = requests.post(
            url,
            json=payload,
            headers=self.headers,
            timeout=10
        )

        if not response.ok:
            print("Pixela status:", response.status_code)
            print("Pixela response:", response.text)

        response.raise_for_status()

        return response.json()
        
    # --------------------------------------------------
    # Update Pixel
    # --------------------------------------------------

    def update_pixel(
        self,
        graph_id: str,
        record_date: str,
        quantity: str
    ):

        url = (
            f"{self.base_url}/users/"
            f"{self.username}/graphs/"
            f"{graph_id}/"
            f"{record_date}"
        )

        payload = {
            "quantity": quantity
        }

        response = requests.put(
            url,
            json=payload,
            headers=self.headers,
            timeout=10
        )

        if not response.ok:
            print("Pixela status:", response.status_code)
            print("Pixela response:", response.text)

        response.raise_for_status()

        return response.json()
    
    # --------------------------------------------------
# Delete Pixel
# --------------------------------------------------

    def delete_pixel(
        self,
        graph_id: str,
        record_date: str
    ):
        """
        Delete a pixel from a Pixela graph.

        Example:
            graph_id = "u1-daily-reading"
            record_date = "20260813"
        """

        url = (
            f"{self.base_url}/users/"
            f"{self.username}/graphs/"
            f"{graph_id}/"
            f"{record_date}"
        )

        response = requests.delete(
            url,
            headers=self.headers,
            timeout=10
        )

        print("Pixela status:", response.status_code)
        print("Pixela response:", response.text)

        response.raise_for_status()

        return response.json()
    
    def get_today_pixel(
    self,
    graph_id: str
    ):
        url = (
            f"{self.base_url}/users/"
            f"{self.username}/graphs/"
            f"{graph_id}/today"
        )

        response = requests.get(
            url,
            headers=self.headers,
            timeout=10
        )

        if response.status_code == 404:
            return None

        response.raise_for_status()

        return response.json()
    
    def get_latest_pixel(
    self,
    graph_id: str
    ):
        url = (
            f"{self.base_url}/users/"
            f"{self.username}/graphs/"
            f"{graph_id}/latest"
        )

        response = requests.get(
            url,
            headers=self.headers,
            timeout=10
        )

        # No latest pixel available
        if response.status_code == 404:
            return None

        response.raise_for_status()

        return response.json()

    
    def get_pixel(
    self,
    graph_id: str,
    record_date: str
    ):
        url = (
            f"{self.base_url}/users/"
            f"{self.username}/graphs/"
            f"{graph_id}/"
            f"{record_date}"
        )

        response = requests.get(
            url,
            headers=self.headers,
            timeout=10
        )

        if response.status_code == 404:
            return None

        response.raise_for_status()

        return response.json()


    def get_pixels(
    self,
    graph_id: str,
    from_date: str | None = None,
    to_date: str | None = None
    ):
        url = (
            f"{self.base_url}/users/"
            f"{self.username}/graphs/"
            f"{graph_id}/pixels"
        )

        params = {
            "withBody": "true"
        }

        if from_date:
            params["from"] = from_date

        if to_date:
            params["to"] = to_date

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=10
        )

        if response.status_code == 404:
            return None

        response.raise_for_status()

        return response.json()
    
    def get_graph_stats(
    self,
    graph_id: str
    ):
        url = (
            f"{self.base_url}/users/"
            f"{self.username}/graphs/"
            f"{graph_id}/stats"
        )

        response = requests.get(
            url,
            headers=self.headers,
            timeout=10
        )

        if response.status_code == 404:
            return None

        response.raise_for_status()

        return response.json()