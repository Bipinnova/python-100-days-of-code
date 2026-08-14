from datetime import date

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.habit import Habit
from app.models.user import User
from app.schemas.habit_record import (
    HabitRecordCreate,
    HabitRecordResponse,
    HabitRecordUpdate,
)
from app.services.habit_record_service import (
    create_record,
    delete_record,
    get_record,
    get_records,
    update_record,
)


router = APIRouter(
    prefix="/habits",
    tags=["Habit Records"]
)


# ---------------------------------------------------------
# Helper: Get User's Habit
# ---------------------------------------------------------

def get_user_habit(
    db: Session,
    user_id: int,
    habit_id: int
) -> Habit | None:

    return (
        db.query(Habit)
        .filter(
            Habit.id == habit_id,
            Habit.user_id == user_id
        )
        .first()
    )


# ---------------------------------------------------------
# Create Habit Record
# ---------------------------------------------------------

@router.post(
    "/{habit_id}/records",
    response_model=HabitRecordResponse,
    status_code=status.HTTP_201_CREATED
)
def create_habit_record(
    habit_id: int,
    record_data: HabitRecordCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Check whether habit belongs to logged-in user
    habit = get_user_habit(
        db,
        current_user.id,
        habit_id
    )

    if not habit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    # Check duplicate record
    existing_record = get_record(
        db,
        habit_id,
        record_data.record_date,
        current_user.id
    )

    if existing_record:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A record already exists for this date"
        )

    # Create PostgreSQL record + Pixela pixel
    return create_record(
        db,
        habit_id,
        current_user.id,
        record_data
    )


# ---------------------------------------------------------
# Get All Habit Records
# ---------------------------------------------------------

@router.get(
    "/{habit_id}/records",
    response_model=list[HabitRecordResponse]
)
def get_habit_records(
    habit_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Check habit ownership
    habit = get_user_habit(
        db,
        current_user.id,
        habit_id
    )

    if not habit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    return get_records(
        db,
        habit_id,
        current_user.id
    )


# ---------------------------------------------------------
# Get Single Habit Record
# ---------------------------------------------------------

@router.get(
    "/{habit_id}/records/{record_date}",
    response_model=HabitRecordResponse
)
def get_single_habit_record(
    habit_id: int,
    record_date: date,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Check habit ownership
    habit = get_user_habit(
        db,
        current_user.id,
        habit_id
    )

    if not habit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    record = get_record(
        db,
        habit_id,
        record_date,
        current_user.id
    )

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )

    return record


# ---------------------------------------------------------
# Update Habit Record
# ---------------------------------------------------------

@router.put(
    "/{habit_id}/records/{record_date}",
    response_model=HabitRecordResponse
)
def update_habit_record(
    habit_id: int,
    record_date: date,
    record_data: HabitRecordUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Check habit ownership
    habit = get_user_habit(
        db,
        current_user.id,
        habit_id
    )

    if not habit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    record = get_record(
        db,
        habit_id,
        record_date,
        current_user.id
    )

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )

    return update_record(
        db,
        record,
        record_data
    )


# ---------------------------------------------------------
# Delete Habit Record
# ---------------------------------------------------------

@router.delete(
    "/{habit_id}/records/{record_date}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_habit_record(
    habit_id: int,
    record_date: date,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    # Check habit ownership
    habit = get_user_habit(
        db,
        current_user.id,
        habit_id
    )

    if not habit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    record = get_record(
        db,
        habit_id,
        record_date,
        current_user.id
    )

    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Record not found"
        )

    delete_record(
        db,
        record
    )

    return None