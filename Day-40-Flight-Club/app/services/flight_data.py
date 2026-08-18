from dataclasses import dataclass


@dataclass
class FlightData:
    price: float
    currency: str

    origin_airport: str
    destination_airport: str

    outbound_date: str

    airline: str | None = None

    duration_minutes: int | None = None

    stops: int = 0