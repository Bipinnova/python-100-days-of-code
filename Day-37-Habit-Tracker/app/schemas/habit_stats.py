from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class HabitStatsResponse(BaseModel):
    habit_id: int
    habit_name: str
    unit: str

    today: Decimal
    total: Decimal
    maximum: Decimal
    minimum: Decimal
    average: Decimal

    total_days: int
    current_streak: int
    longest_streak: int