from decimal import Decimal

from pydantic import BaseModel


class HabitDashboardItem(BaseModel):
    habit_id: int
    habit_name: str
    description: str | None
    unit: str
    pixela_graph_id: str

    # Pixela graph URL
    pixela_url: str

    # PostgreSQL statistics
    today: Decimal
    total: Decimal
    maximum: Decimal
    minimum: Decimal
    average: Decimal

    total_days: int
    current_streak: int
    longest_streak: int

    # Pixela statistics
    pixela_total: Decimal
    pixela_total_days: int

    # Progress
    today_progress_percentage: float


class MultipleHabitsDashboardResponse(BaseModel):
    total_habits: int
    habits: list[HabitDashboardItem]