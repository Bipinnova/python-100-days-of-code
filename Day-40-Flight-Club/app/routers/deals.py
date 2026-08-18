from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.customer import Customer
from app.models.flight import FlightRoute

from app.schemas.deal import (
    DealCheckAllResponse,
    DealCheckResponse
)

from app.services.deal_service import DealService
from app.services.flight_search import FlightSearch
from app.services.notification_manager import (
    NotificationManager
)


router = APIRouter(
    prefix="/api/v1/deals",
    tags=["Flight Deals"]
)


flight_search = FlightSearch()

deal_service = DealService(
    flight_search
)

notification_manager = (
    NotificationManager()
)


@router.post(
    "/check/{route_id}",
    response_model=DealCheckResponse
)
def check_deal(
    route_id: int,
    outbound_date: date,
    db: Session = Depends(get_db)
):

    route = (
        db.query(FlightRoute)
        .filter(
            FlightRoute.id == route_id,
            FlightRoute.is_active == True
        )
        .first()
    )

    if not route:

        raise HTTPException(
            status_code=404,
            detail="Active flight route not found."
        )

    flight, is_deal = (
        deal_service.check_route_deal(
            db=db,
            route=route,
            flight_date=outbound_date.strftime(
                "%Y-%m-%d"
            )
        )
    )

    if not flight:

        raise HTTPException(
            status_code=404,
            detail=(
                f"No flight found for "
                f"{route.from_iata} → "
                f"{route.to_iata}"
            )
        )

    notification_sent = False

    if is_deal:

        customers = (
            db.query(Customer)
            .filter(
                Customer.is_active == True
            )
            .all()
        )

        notification_manager.send_to_customers(
            customers=customers,
            flight=flight
        )

        # Also send WhatsApp to your own number.
        try:

            notification_manager.send_whatsapp(
                flight
            )

            notification_sent = True

        except Exception as error:

            print(
                f"Twilio notification failed: "
                f"{error}"
            )

    if is_deal:

        message = (
            f"Cheap flight found! "
            f"{route.from_iata} → "
            f"{route.to_iata} "
            f"for ₹{flight.price:,.0f}."
        )

    else:

        message = (
            f"No new cheaper flight found. "
            f"Current price: "
            f"₹{flight.price:,.0f}."
        )

    return DealCheckResponse(

        route_id=route.id,

        from_city=route.from_city,
        from_iata=route.from_iata,

        to_city=route.to_city,
        to_iata=route.to_iata,

        target_price=route.target_price,

        current_price=flight.price,

        currency=flight.currency,

        airline=flight.airline,

        outbound_date=flight.outbound_date,

        duration_minutes=(
            flight.duration_minutes
        ),

        stops=flight.stops,

        is_deal=is_deal,

        notification_sent=notification_sent,

        message=message
    )


@router.post(
    "/check-all",
    response_model=DealCheckAllResponse
)
def check_all_deals(
    outbound_date: date,
    db: Session = Depends(get_db)
):

    routes = (
        db.query(FlightRoute)
        .filter(
            FlightRoute.is_active == True
        )
        .order_by(FlightRoute.id)
        .all()
    )

    if not routes:

        raise HTTPException(
            status_code=404,
            detail="No active flight routes found."
        )

    customers = (
        db.query(Customer)
        .filter(
            Customer.is_active == True
        )
        .all()
    )

    results = []

    deals_found = 0

    notifications_sent = 0

    for route in routes:

        print(
            f"\nChecking route: "
            f"{route.from_iata} → "
            f"{route.to_iata}"
        )

        try:

            flight, is_deal = (
                deal_service.check_route_deal(
                    db=db,
                    route=route,
                    flight_date=outbound_date.strftime(
                        "%Y-%m-%d"
                    )
                )
            )

            if not flight:

                continue

            notification_sent = False

            if is_deal:

                deals_found += 1

                # Email customers.
                email_count = (
                    notification_manager
                    .send_to_customers(
                        customers=customers,
                        flight=flight
                    )
                )

                # WhatsApp notification.
                try:

                    notification_manager.send_whatsapp(
                        flight
                    )

                    notification_sent = True

                except Exception as error:

                    print(
                        f"Twilio failed: {error}"
                    )

                notifications_sent += (
                    email_count
                )

            if is_deal:

                message = (
                    f"Cheap flight found! "
                    f"₹{flight.price:,.0f}"
                )

            else:

                message = (
                    f"No new cheaper flight."
                )

            results.append(
                DealCheckResponse(

                    route_id=route.id,

                    from_city=route.from_city,
                    from_iata=route.from_iata,

                    to_city=route.to_city,
                    to_iata=route.to_iata,

                    target_price=(
                        route.target_price
                    ),

                    current_price=(
                        flight.price
                    ),

                    currency=flight.currency,

                    airline=flight.airline,

                    outbound_date=(
                        flight.outbound_date
                    ),

                    duration_minutes=(
                        flight.duration_minutes
                    ),

                    stops=flight.stops,

                    is_deal=is_deal,

                    notification_sent=(
                        notification_sent
                    ),

                    message=message
                )
            )

        except Exception as error:

            print(
                f"Failed route "
                f"{route.id}: {error}"
            )

    return DealCheckAllResponse(

        checked_routes=len(routes),

        deals_found=deals_found,

        notifications_sent=(
            notifications_sent
        ),

        results=results
    )
    

@router.post(
    "/test-notification"
)
def test_notification(
    db: Session = Depends(get_db)
):

    route = (
        db.query(FlightRoute)
        .filter(
            FlightRoute.is_active == True
        )
        .first()
    )

    if not route:

        raise HTTPException(
            status_code=404,
            detail="No active flight route found."
        )

    from app.services.flight_data import FlightData

    test_flight = FlightData(

        price=4500.0,

        currency="INR",

        origin_airport=(
            route.from_iata
        ),

        destination_airport=(
            route.to_iata
        ),

        outbound_date="2026-09-15",

        airline="Test Airline",

        duration_minutes=140,

        stops=0
    )

    whatsapp_sent = False

    email_count = 0

    try:

        notification_manager.send_whatsapp(
            test_flight
        )

        whatsapp_sent = True

    except Exception as error:

        print(
            f"Twilio test failed: {error}"
        )

    customers = (
        db.query(Customer)
        .filter(
            Customer.is_active == True
        )
        .all()
    )

    try:

        email_count = (
            notification_manager
            .send_to_customers(
                customers=customers,
                flight=test_flight
            )
        )

    except Exception as error:

        print(
            f"Email test failed: {error}"
        )

    return {
        "message": (
            "Notification test completed."
        ),
        "whatsapp_sent": whatsapp_sent,
        "emails_sent": email_count
    }