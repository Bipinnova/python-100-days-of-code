from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.habit import (
    HabitCreate,
    HabitResponse,
    HabitUpdate,
)

from app.services.habit_service import (
    create_habit,
    get_user_habits,
    get_habit,
    update_habit,
    delete_habit,
)


router = APIRouter(
    prefix="/habits",
    tags=["Habits"]
)


@router.post(
    "/",
    response_model=HabitResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_habit(
    habit_data: HabitCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = create_habit(
        db=db,
        user_id=current_user.id,
        habit_data=habit_data
    )

    return habit


@router.get(
    "/",
    response_model=list[HabitResponse]
)
def get_habits(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_habits(
        db=db,
        user_id=current_user.id
    )


@router.get(
    "/{habit_id}",
    response_model=HabitResponse
)
def get_habit(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = get_user_habit(
        db=db,
        user_id=current_user.id,
        habit_id=habit_id
    )

    if not habit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    return habit


@router.put(
    "/{habit_id}",
    response_model=HabitResponse
)
def update_existing_habit(
    habit_id: int,
    habit_data: HabitUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = get_user_habit(
        db=db,
        user_id=current_user.id,
        habit_id=habit_id
    )

    if not habit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    return update_habit(
        db=db,
        habit=habit,
        habit_data=habit_data
    )


@router.delete(
    "/{habit_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_existing_habit(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    habit = get_user_habit(
        db=db,
        user_id=current_user.id,
        habit_id=habit_id
    )

    if not habit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    delete_habit(
        db=db,
        habit=habit
    )

    return None