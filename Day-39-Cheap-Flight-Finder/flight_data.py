from dataclasses import dataclass
from typing import Optional


@dataclass
class FlightData:
    price: float
    currency: str
    origin_airport: str
    destination_airport: str
    outbound_date: str
    airline: Optional[str] = None
    duration_minutes: Optional[int] = None