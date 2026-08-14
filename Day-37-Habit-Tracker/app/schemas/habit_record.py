from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class HabitRecordCreate(BaseModel):
    record_date: date

    quantity: Decimal = Field(
        gt=0,
        max_digits=10,
        decimal_places=2
    )


class HabitRecordUpdate(BaseModel):
    quantity: Decimal = Field(
        gt=0,
        max_digits=10,
        decimal_places=2
    )


class HabitRecordResponse(BaseModel):
    id: int
    habit_id: int
    record_date: date
    quantity: Decimal
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True