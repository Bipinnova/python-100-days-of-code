from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.habit import Habit
from app.services.habit_stats_service import get_habit_stats
from app.services.pixela_service import PixelaService
from app.core.config import (
    PIXELA_BASE_URL,
    PIXELA_USERNAME,
)


def get_habit_dashboard(
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
    # Pixela graph URL
    # --------------------------------------------------

    pixela_url = (
        f"{PIXELA_BASE_URL}/users/"
        f"{PIXELA_USERNAME}/graphs/"
        f"{habit.pixela_graph_id}.html"
    )

    # --------------------------------------------------
    # Get PostgreSQL statistics
    # --------------------------------------------------

    db_stats = get_habit_stats(
        db=db,
        habit_id=habit_id,
        user_id=user_id
    )

    # --------------------------------------------------
    # Get Pixela statistics
    # --------------------------------------------------

    pixela_service = PixelaService()

    pixela_stats = pixela_service.get_graph_stats(
        graph_id=habit.pixela_graph_id
    )

    # --------------------------------------------------
    # Default Pixela values
    # --------------------------------------------------

    pixela_total = Decimal("0")
    pixela_maximum = Decimal("0")
    pixela_minimum = Decimal("0")
    pixela_average = Decimal("0")
    pixela_total_days = 0

    if pixela_stats:

        pixela_total = Decimal(
            str(
                pixela_stats.get(
                    "totalQuantity",
                    0
                )
            )
        )

        pixela_maximum = Decimal(
            str(
                pixela_stats.get(
                    "maxQuantity",
                    0
                )
            )
        )

        pixela_minimum = Decimal(
            str(
                pixela_stats.get(
                    "minQuantity",
                    0
                )
            )
        )

        pixela_average = Decimal(
            str(
                pixela_stats.get(
                    "averageQuantity",
                    0
                )
            )
        )

        pixela_total_days = int(
            pixela_stats.get(
                "totalPixels",
                0
            )
        )

    # --------------------------------------------------
    # Calculate today's progress
    # --------------------------------------------------

    today_progress_percentage = 0.0

    if db_stats["today"] > 0:

        today_progress_percentage = 100.0

    # --------------------------------------------------
    # Final dashboard response
    # --------------------------------------------------
    
    

    return {
        "habit_id": habit.id,
        "habit_name": habit.name,
        "description": habit.description,
        "unit": habit.unit,
        "pixela_graph_id": habit.pixela_graph_id,
        "pixela_url": pixela_url,

        # PostgreSQL
        "today": db_stats["today"],
        "total": db_stats["total"],
        "maximum": db_stats["maximum"],
        "minimum": db_stats["minimum"],
        "average": db_stats["average"],

        "total_days": db_stats["total_days"],
        "current_streak": db_stats["current_streak"],
        "longest_streak": db_stats["longest_streak"],

        # Pixela
        "pixela_total": pixela_total,
        "pixela_maximum": pixela_maximum,
        "pixela_minimum": pixela_minimum,
        "pixela_average": pixela_average,
        "pixela_total_days": pixela_total_days,

        # Progress
        "today_progress_percentage":
            today_progress_percentage
    }