import os

import requests
import requests_cache
from dotenv import load_dotenv

from flight_data import FlightData


load_dotenv()


requests_cache.install_cache(
    "flight_search_cache",
    expire_after=3600
)


class FlightSearch:

    def __init__(self):

        self.api_key = os.getenv("SERPAPI_KEY")

        if not self.api_key:
            raise ValueError(
                "SERPAPI_KEY is missing in .env"
            )

        self.endpoint = "https://serpapi.com/search.json"

    def search_flights(
        self,
        origin: str,
        destination: str,
        outbound_date: str
    ) -> FlightData | None:

        params = {
            "engine": "google_flights",
            "departure_id": origin,
            "arrival_id": destination,
            "outbound_date": outbound_date,
            "currency": "INR",
            "hl": "en",
            "gl": "in",
            "type": "2",
            "travel_class": "1",
            "api_key": self.api_key,
        }

        response = requests.get(
            self.endpoint,
            params=params,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        if "error" in data:
            raise RuntimeError(
                f"SerpAPI error: {data['error']}"
            )

        best_flights = data.get(
            "best_flights",
            []
        )

        if not best_flights:
            return None

        cheapest_flight = min(
            best_flights,
            key=lambda flight: flight.get(
                "price",
                float("inf")
            )
        )

        price = cheapest_flight.get("price")

        if price is None:
            return None

        flight_segments = cheapest_flight.get(
            "flights",
            []
        )

        if not flight_segments:
            return None

        first_segment = flight_segments[0]

        airline = first_segment.get(
            "airline"
        )

        duration = cheapest_flight.get(
            "total_duration"
        )

        return FlightData(
            price=float(price),
            currency="INR",
            origin_airport=origin,
            destination_airport=destination,
            outbound_date=outbound_date,
            airline=airline,
            duration_minutes=duration,
        )