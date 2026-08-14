from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.dashboard import (
    MultipleHabitsDashboardResponse
)
from app.schemas.habit_dashboard import (
    HabitDashboardResponse
)
from app.services.dashboard_service import (
    get_user_dashboard
)
from app.services.habit_dashboard_service import (
    get_habit_dashboard
)


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "",
    response_model=MultipleHabitsDashboardResponse
)
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_user_dashboard(
        db=db,
        user_id=current_user.id
    )


@router.get(
    "/habits/{habit_id}",
    response_model=HabitDashboardResponse
)
def get_single_habit_dashboard(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return get_habit_dashboard(
        db=db,
        habit_id=habit_id,
        user_id=current_user.id
    )