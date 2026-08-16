from datetime import date

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


app = FastAPI(
    title="Cheap Flight Finder API",
    description="Find cheap one-way flights and send notifications.",
    version="1.0.0"
)


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()


class FlightSearchRequest(BaseModel):

    from_iata: str = Field(
        ...,
        min_length=3,
        max_length=3,
        description="Departure airport IATA code"
    )

    to_iata: str = Field(
        ...,
        min_length=3,
        max_length=3,
        description="Destination airport IATA code"
    )

    outbound_date: date


@app.get("/", include_in_schema=False)
def home():

    return {
        "message": "Cheap Flight Finder API",
        "docs": "/docs"
    }


@app.get("/flights/sheet")
def get_sheet_flights():

    flights = data_manager.get_flight_data()

    return {
        "count": len(flights),
        "flights": flights
    }


@app.post("/flights/search")
def search_flight(
    request: FlightSearchRequest
):

    flight = flight_search.search_flights(
        origin=request.from_iata.upper(),
        destination=request.to_iata.upper(),
        outbound_date=request.outbound_date.strftime(
            "%Y-%m-%d"
        )
    )

    if not flight:

        raise HTTPException(
            status_code=404,
            detail="No flight found."
        )

    return {
        "price": flight.price,
        "currency": flight.currency,
        "origin_airport": flight.origin_airport,
        "destination_airport": flight.destination_airport,
        "outbound_date": flight.outbound_date,
        "airline": flight.airline,
        "duration_minutes": flight.duration_minutes
    }


@app.post("/flights/check-deal")
def check_deal(
    request: FlightSearchRequest
):

    # 1. Search one-way flight
    flight = flight_search.search_flights(
        origin=request.from_iata.upper(),
        destination=request.to_iata.upper(),
        outbound_date=request.outbound_date.strftime(
            "%Y-%m-%d"
        )
    )

    if not flight:

        raise HTTPException(
            status_code=404,
            detail="No flight found."
        )

    # 2. Read routes from Google Sheet
    destinations = data_manager.get_flight_data()

    # 3. Find matching route
    matching_route = None

    for destination in destinations:

        if (
            destination["fromIata"].upper()
            == request.from_iata.upper()
            and
            destination["toIata"].upper()
            == request.to_iata.upper()
        ):
            matching_route = destination
            break

    if not matching_route:

        raise HTTPException(
            status_code=404,
            detail="Route not found in Google Sheet."
        )

    # 4. Get lowest price from Google Sheet
    lowest_price = float(
        matching_route["lowestPrice"]
    )

    # 5. Compare flight price
    if flight.price < lowest_price:

        message = (
            "✈️ CHEAP FLIGHT ALERT!\n\n"
            f"{flight.origin_airport} → "
            f"{flight.destination_airport}\n"
            f"Price: ₹{flight.price:,.0f}\n"
            f"Airline: {flight.airline}\n"
            f"Departure: {flight.outbound_date}\n"
            f"Duration: {flight.duration_minutes} minutes\n\n"
            f"Previous lowest price: "
            f"₹{lowest_price:,.0f}"
        )

        message_sid = (
            notification_manager
            .send_notification(message)
        )

        return {
            "deal_found": True,
            "message": "Cheap flight found! Notification sent.",
            "flight_price": flight.price,
            "lowest_price": lowest_price,
            "route": (
                f"{flight.origin_airport} → "
                f"{flight.destination_airport}"
            ),
            "airline": flight.airline,
            "outbound_date": flight.outbound_date,
            "duration_minutes": flight.duration_minutes,
            "message_sid": message_sid
        }

    # 6. No cheaper flight
    return {
        "deal_found": False,
        "message": "No cheaper flight found.",
        "flight_price": flight.price,
        "lowest_price": lowest_price,
        "route": (
            f"{flight.origin_airport} → "
            f"{flight.destination_airport}"
        ),
        "airline": flight.airline,
        "outbound_date": flight.outbound_date,
        "duration_minutes": flight.duration_minutes
    }