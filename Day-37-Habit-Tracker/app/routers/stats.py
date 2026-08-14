from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.habit_stats import HabitStatsResponse
from app.services.habit_stats_service import get_habit_stats


router = APIRouter(
    prefix="/habits",
    tags=["Habit Statistics"]
)


@router.get(
    "/{habit_id}/stats",
    response_model=HabitStatsResponse
)
def get_stats(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_habit_stats(
        db=db,
        habit_id=habit_id,
        user_id=current_user.id
    )