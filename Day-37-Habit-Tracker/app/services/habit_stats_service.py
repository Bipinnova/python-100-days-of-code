from datetime import date, timedelta
from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.habit import Habit
from app.models.habit_record import HabitRecord


def get_habit_stats(
    db: Session,
    habit_id: int,
    user_id: int
):
    # --------------------------------------------------
    # Get habit
    # --------------------------------------------------

    habit = (
        db.query(Habit)
        .filter(
            Habit.id == habit_id,
            Habit.user_id == user_id
        )
        .first()
    )

    if not habit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    # --------------------------------------------------
    # Get all records
    # --------------------------------------------------

    records = (
        db.query(HabitRecord)
        .filter(
            HabitRecord.habit_id == habit_id
        )
        .order_by(
            HabitRecord.record_date.asc()
        )
        .all()
    )

    # --------------------------------------------------
    # No records
    # --------------------------------------------------

    if not records:
        return {
            "habit_id": habit.id,
            "habit_name": habit.name,
            "unit": habit.unit,
            "today": Decimal("0"),
            "total": Decimal("0"),
            "maximum": Decimal("0"),
            "minimum": Decimal("0"),
            "average": Decimal("0"),
            "total_days": 0,
            "current_streak": 0,
            "longest_streak": 0
        }

    # --------------------------------------------------
    # Basic statistics
    # --------------------------------------------------

    quantities = [
        record.quantity
        for record in records
    ]

    total = sum(
        quantities,
        Decimal("0")
    )

    maximum = max(quantities)

    minimum = min(quantities)

    average = total / Decimal(len(quantities))

    # --------------------------------------------------
    # Today's quantity
    # --------------------------------------------------

    today_record = (
        db.query(HabitRecord)
        .filter(
            HabitRecord.habit_id == habit_id,
            HabitRecord.record_date == date.today()
        )
        .first()
    )

    today_quantity = (
        today_record.quantity
        if today_record
        else Decimal("0")
    )

    # --------------------------------------------------
    # Total days
    # --------------------------------------------------

    total_days = len(records)

    # --------------------------------------------------
    # Streak calculation
    # --------------------------------------------------

    record_dates = {
        record.record_date
        for record in records
    }

    current_streak = calculate_current_streak(
        record_dates
    )

    longest_streak = calculate_longest_streak(
        record_dates
    )

    return {
        "habit_id": habit.id,
        "habit_name": habit.name,
        "unit": habit.unit,
        "today": today_quantity,
        "total": total,
        "maximum": maximum,
        "minimum": minimum,
        "average": average,
        "total_days": total_days,
        "current_streak": current_streak,
        "longest_streak": longest_streak
    }


def calculate_current_streak(
    record_dates: set[date]
) -> int:

    if not record_dates:
        return 0

    today = date.today()

    # If there is no record today, current streak is 0.
    if today not in record_dates:
        return 0

    streak = 0
    current_date = today

    while current_date in record_dates:

        streak += 1

        current_date -= timedelta(days=1)

    return streak


def calculate_longest_streak(
    record_dates: set[date]
) -> int:

    if not record_dates:
        return 0

    sorted_dates = sorted(record_dates)

    longest_streak = 1
    current_streak = 1

    for index in range(1, len(sorted_dates)):

        previous_date = sorted_dates[index - 1]
        current_date = sorted_dates[index]

        if current_date == previous_date + timedelta(days=1):

            current_streak += 1

        else:

            current_streak = 1

        longest_streak = max(
            longest_streak,
            current_streak
        )

    return longest_streak