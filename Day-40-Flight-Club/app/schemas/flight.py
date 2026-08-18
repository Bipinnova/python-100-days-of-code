from pydantic import BaseModel, Field


class FlightRouteCreate(BaseModel):

    from_city: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    from_iata: str = Field(
        ...,
        min_length=3,
        max_length=3
    )

    to_city: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    to_iata: str = Field(
        ...,
        min_length=3,
        max_length=3
    )

    target_price: float = Field(
        ...,
        gt=0
    )

    currency: str = Field(
        default="INR",
        max_length=10
    )


class FlightRouteUpdate(BaseModel):

    from_city: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    from_iata: str | None = Field(
        default=None,
        min_length=3,
        max_length=3
    )

    to_city: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    to_iata: str | None = Field(
        default=None,
        min_length=3,
        max_length=3
    )

    target_price: float | None = Field(
        default=None,
        gt=0
    )

    currency: str | None = Field(
        default=None,
        max_length=10
    )

    is_active: bool | None = None


class FlightRouteResponse(BaseModel):

    id: int

    from_city: str
    from_iata: str

    to_city: str
    to_iata: str

    target_price: float
    lowest_price: float

    currency: str
    is_active: bool

    class Config:
        from_attributes = True