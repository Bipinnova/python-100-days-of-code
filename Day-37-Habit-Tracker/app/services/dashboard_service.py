from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.habit import Habit
from app.services.habit_dashboard_service import (
    get_habit_dashboard
)


def get_user_dashboard(
    db: Session,
    user_id: int
):

    habits = (
        db.query(Habit)
        .filter(
            Habit.user_id == user_id
        )
        .order_by(
            Habit.id.asc()
        )
        .all()
    )

    dashboard_habits = []

    for habit in habits:

        dashboard_data = get_habit_dashboard(
            db=db,
            habit_id=habit.id,
            user_id=user_id
        )

        dashboard_habits.append(
            dashboard_data
        )

    return {
        "total_habits": len(dashboard_habits),
        "habits": dashboard_habits
    }