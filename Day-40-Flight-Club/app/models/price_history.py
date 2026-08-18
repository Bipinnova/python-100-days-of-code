from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class FlightPriceHistory(Base):

    __tablename__ = "flight_price_history"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    flight_route_id: Mapped[int] = mapped_column(
        ForeignKey(
            "flight_routes.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="INR",
        nullable=False
    )

    airline: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    outbound_date: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    stops: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False
    )

    duration_minutes: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    searched_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )