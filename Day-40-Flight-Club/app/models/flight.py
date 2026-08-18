from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class FlightRoute(Base):

    __tablename__ = "flight_routes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    from_city: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    from_iata: Mapped[str] = mapped_column(
        String(3),
        nullable=False
    )

    to_city: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    to_iata: Mapped[str] = mapped_column(
        String(3),
        nullable=False
    )

    target_price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    lowest_price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        default="INR",
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )