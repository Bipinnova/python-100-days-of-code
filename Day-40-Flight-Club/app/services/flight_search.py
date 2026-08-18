import os

import requests
import requests_cache
from dotenv import load_dotenv

from app.services.flight_data import FlightData


load_dotenv()


# Cache identical API requests for 1 hour.
# This helps avoid unnecessary SerpAPI requests during development.
requests_cache.install_cache(
    "flight_search_cache",
    expire_after=3600
)


class FlightSearch:

    def __init__(self):

        self.api_key = os.getenv(
            "SERPAPI_KEY"
        )

        if not self.api_key:
            raise ValueError(
                "SERPAPI_KEY is missing in .env"
            )

        self.endpoint = (
            "https://serpapi.com/search.json"
        )

    def check_flights(
        self,
        origin_city_code: str,
        destination_city_code: str,
        flight_date: str,
        is_direct: bool = True
    ) -> FlightData | None:

        # SerpAPI:
        # stops=0 -> direct/non-stop
        # stops=1 -> flights with stops

        stops = "0" if is_direct else "1"

        params = {
            "engine": "google_flights",

            "departure_id": (
                origin_city_code.upper()
            ),

            "arrival_id": (
                destination_city_code.upper()
            ),

            "outbound_date": flight_date,

            "currency": "INR",

            "hl": "en",

            "gl": "in",

            "type": "2",

            "stops": stops,

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

                # Find the cheapest flight.
        valid_flights = []

        for flight in best_flights:

            flight_segments = flight.get(
                "flights",
                []
            )

            if not flight_segments:
                continue

            number_of_stops = (
                len(flight_segments) - 1
            )

            if is_direct and number_of_stops == 0:
                valid_flights.append(flight)

            elif not is_direct and number_of_stops > 0:
                valid_flights.append(flight)
                
        if not valid_flights:
            return None

        cheapest_flight = min(
            valid_flights,
            key=lambda flight: flight.get(
                "price",
                float("inf")
            )
        )

        price = cheapest_flight.get(
            "price"
        )

        if price is None:

            return None

        flight_segments = (
            cheapest_flight.get(
                "flights",
                []
            )
        )

        if not flight_segments:

            return None

        # Number of stops:
        #
        # 1 segment = 0 stops
        # 2 segments = 1 stop
        # 3 segments = 2 stops

        number_of_stops = (
            len(flight_segments) - 1
        )

        first_segment = (
            flight_segments[0]
        )

        airline = first_segment.get(
            "airline"
        )

        duration = cheapest_flight.get(
            "total_duration"
        )

        return FlightData(
            price=float(price),

            currency="INR",

            origin_airport=(
                origin_city_code.upper()
            ),

            destination_airport=(
                destination_city_code.upper()
            ),

            outbound_date=flight_date,

            airline=airline,

            duration_minutes=duration,

            stops=number_of_stops
        )


if __name__ == "__main__":

    flight_search = FlightSearch()

    flight = flight_search.check_flights(
        origin_city_code="BOM",
        destination_city_code="VNS",
        flight_date="2026-09-15",
        is_direct=True
        #is_direct=False
    )

    print("\nDIRECT FLIGHT RESULT")
    print("=" * 50)

    if flight:

        print(
            f"Price: ₹{flight.price:,.0f}"
        )

        print(
            f"Route: "
            f"{flight.origin_airport} → "
            f"{flight.destination_airport}"
        )

        print(
            f"Date: {flight.outbound_date}"
        )

        print(
            f"Airline: {flight.airline}"
        )

        print(
            f"Duration: "
            f"{flight.duration_minutes} minutes"
        )

        print(
            f"Stops: {flight.stops}"
        )

    else:

        print(
            "No direct flight found."
        )