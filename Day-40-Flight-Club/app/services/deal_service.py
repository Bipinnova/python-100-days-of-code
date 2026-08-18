from sqlalchemy.orm import Session

from app.models.price_history import FlightPriceHistory
from app.models.flight import FlightRoute
from app.services.flight_data import FlightData
from app.services.flight_search import FlightSearch


class DealService:

    def __init__(self, flight_search: FlightSearch):
        self.flight_search = flight_search

    def find_best_flight(
        self,
        origin_iata: str,
        destination_iata: str,
        flight_date: str
    ) -> FlightData | None:

        print(
            f"Getting direct flight "
            f"for {destination_iata}..."
        )

        # First search direct flights.
        cheapest_flight = self.flight_search.check_flights(
            origin_city_code=origin_iata,
            destination_city_code=destination_iata,
            flight_date=flight_date,
            is_direct=True
        )

        if cheapest_flight:
            return cheapest_flight

        # If no direct flight is found,
        # search for indirect flights.
        print(
            f"No direct flight to "
            f"{destination_iata}. "
            f"Looking for indirect flights..."
        )

        cheapest_flight = self.flight_search.check_flights(
            origin_city_code=origin_iata,
            destination_city_code=destination_iata,
            flight_date=flight_date,
            is_direct=False
        )

        return cheapest_flight

    def check_route_deal(
        self,
        db: Session,
        route: FlightRoute,
        flight_date: str
    ) -> tuple[FlightData | None, bool]:

        # Search flight.
        flight = self.find_best_flight(
            origin_iata=route.from_iata,
            destination_iata=route.to_iata,
            flight_date=flight_date
        )

        # No flight found.
        if not flight:

            print(
                f"No flight found for "
                f"{route.from_iata} → "
                f"{route.to_iata}"
            )

            return None, False

        print(
            f"Found flight: "
            f"{route.from_iata} → "
            f"{route.to_iata}"
        )

        print(
            f"Price: ₹{flight.price:,.0f}"
        )

        print(
            f"Target price: "
            f"₹{route.target_price:,.0f}"
        )

        # ------------------------------------------------
        # Save flight price history
        # ------------------------------------------------

        price_history = FlightPriceHistory(

            flight_route_id=route.id,

            price=flight.price,

            currency=flight.currency,

            airline=flight.airline,

            outbound_date=flight.outbound_date,

            stops=flight.stops,

            duration_minutes=(
                flight.duration_minutes
            )
        )

        db.add(price_history)

        # ------------------------------------------------
        # Update lowest price
        # ------------------------------------------------

        if (
            route.lowest_price is None
            or flight.price < route.lowest_price
        ):

            route.lowest_price = flight.price

            print(
                f"Lowest price updated to "
                f"₹{flight.price:,.0f}"
            )

        # Save database changes.
        db.commit()

        db.refresh(route)

        # ------------------------------------------------
        # Check deal
        # ------------------------------------------------

        is_deal = (
            flight.price < route.target_price
        )

        if is_deal:

            print(
                "🎉 CHEAP FLIGHT FOUND!"
            )

            print(
                f"{route.from_iata} → "
                f"{route.to_iata}"
            )

            print(
                f"Price: "
                f"₹{flight.price:,.0f}"
            )

        else:

            print(
                "No deal found."
            )

        return flight, is_deal