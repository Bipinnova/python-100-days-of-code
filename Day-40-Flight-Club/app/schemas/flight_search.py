from datetime import date

from pydantic import BaseModel, Field


class FlightSearchRequest(BaseModel):

    from_iata: str = Field(
        ...,
        min_length=3,
        max_length=3
    )

    to_iata: str = Field(
        ...,
        min_length=3,
        max_length=3
    )

    outbound_date: date
    
class FlightSearchResponse(BaseModel):

    price: float

    currency: str

    origin_airport: str

    destination_airport: str

    outbound_date: str

    airline: str | None

    duration_minutes: int | None

    stops: int