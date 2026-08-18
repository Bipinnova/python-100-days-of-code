from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.flight import FlightRoute
from app.schemas.flight import (
    FlightRouteCreate,
    FlightRouteUpdate,
    FlightRouteResponse,
)
from datetime import date

from app.services.deal_service import DealService
from app.services.flight_search import FlightSearch

from app.schemas.flight_search import (
    FlightSearchRequest,
    FlightSearchResponse,
)

router = APIRouter(
    prefix="/api/v1/routes",
    tags=["Flight Routes"]
)

flight_search = FlightSearch()

deal_service = DealService(
    flight_search
)

@router.post(
    "",
    response_model=FlightRouteResponse,
    status_code=201
)
def create_route(
    route: FlightRouteCreate,
    db: Session = Depends(get_db)
):

    new_route = FlightRoute(
    from_city=route.from_city,
    from_iata=route.from_iata.upper(),
    to_city=route.to_city,
    to_iata=route.to_iata.upper(),

    target_price=route.target_price,

    # Initially lowest found price
    # is the target price.
    lowest_price=route.target_price,

    currency=route.currency.upper(),
    )

    db.add(new_route)
    db.commit()
    db.refresh(new_route)

    return new_route


@router.get(
    "",
    response_model=list[FlightRouteResponse]
)
def get_routes(
    db: Session = Depends(get_db)
):

    routes = (
        db.query(FlightRoute)
        .order_by(FlightRoute.id)
        .all()
    )

    return routes


@router.post(
    "/search",
    response_model=FlightSearchResponse
)
def search_flight(
    request: FlightSearchRequest
):

    flight = deal_service.find_best_flight(
        origin_iata=request.from_iata.upper(),
        destination_iata=request.to_iata.upper(),
        flight_date=request.outbound_date.strftime(
            "%Y-%m-%d"
        )
    )

    if not flight:

        raise HTTPException(
            status_code=404,
            detail="No flight found."
        )

    return flight


@router.get(
    "/{route_id}",
    response_model=FlightRouteResponse
)
def get_route(
    route_id: int,
    db: Session = Depends(get_db)
):

    route = (
        db.query(FlightRoute)
        .filter(
            FlightRoute.id == route_id
        )
        .first()
    )

    if not route:

        raise HTTPException(
            status_code=404,
            detail="Flight route not found."
        )

    return route


@router.put(
    "/{route_id}",
    response_model=FlightRouteResponse
)
def update_route(
    route_id: int,
    route_data: FlightRouteUpdate,
    db: Session = Depends(get_db)
):

    route = (
        db.query(FlightRoute)
        .filter(
            FlightRoute.id == route_id
        )
        .first()
    )

    if not route:

        raise HTTPException(
            status_code=404,
            detail="Flight route not found."
        )

    update_data = route_data.model_dump(
        exclude_unset=True
    )

    if "from_iata" in update_data:
        update_data["from_iata"] = (
            update_data["from_iata"].upper()
        )

    if "to_iata" in update_data:
        update_data["to_iata"] = (
            update_data["to_iata"].upper()
        )

    if "currency" in update_data:
        update_data["currency"] = (
            update_data["currency"].upper()
        )

    for field, value in update_data.items():

        setattr(
            route,
            field,
            value
        )

    db.commit()
    db.refresh(route)

    return route


@router.delete(
    "/{route_id}"
)
def delete_route(
    route_id: int,
    db: Session = Depends(get_db)
):

    route = (
        db.query(FlightRoute)
        .filter(
            FlightRoute.id == route_id
        )
        .first()
    )

    if not route:

        raise HTTPException(
            status_code=404,
            detail="Flight route not found."
        )

    db.delete(route)
    db.commit()

    return {
        "message": "Flight route deleted successfully.",
        "route_id": route_id
    }
    
    