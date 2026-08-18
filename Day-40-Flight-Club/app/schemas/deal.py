from pydantic import BaseModel


class DealCheckResponse(BaseModel):

    route_id: int

    from_city: str
    from_iata: str

    to_city: str
    to_iata: str

    target_price: float
    current_price: float

    currency: str

    airline: str | None

    outbound_date: str

    duration_minutes: int | None

    stops: int

    is_deal: bool

    notification_sent: bool

    message: str


class DealCheckAllResponse(BaseModel):

    checked_routes: int

    deals_found: int

    notifications_sent: int

    results: list[DealCheckResponse]