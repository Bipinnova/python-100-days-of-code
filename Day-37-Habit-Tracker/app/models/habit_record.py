from datetime import date, datetime

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKey,
    Numeric,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class HabitRecord(Base):
    __tablename__ = "habit_records"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    habit_id: Mapped[int] = mapped_column(
        ForeignKey(
            "habits.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )

    record_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True
    )

    quantity: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint(
            "habit_id",
            "record_date",
            name="uq_habit_record_date"
        ),
    )