from datetime import date

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.habit import Habit
from app.models.habit_record import HabitRecord
from app.schemas.habit_record import (
    HabitRecordCreate,
    HabitRecordUpdate,
)
from app.services.pixela_service import PixelaService


# ---------------------------------------------------------
# Create Habit Record
# ---------------------------------------------------------

def create_record(
    db: Session,
    habit_id: int,
    user_id: int,
    record_data: HabitRecordCreate
) -> HabitRecord:

    # -----------------------------------------------------
    # 1. Find the habit
    # -----------------------------------------------------

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

    # -----------------------------------------------------
    # 2. Check if record already exists for this date
    # -----------------------------------------------------

    existing_record = (
        db.query(HabitRecord)
        .filter(
            HabitRecord.habit_id == habit_id,
            HabitRecord.record_date == record_data.record_date
        )
        .first()
    )

    if existing_record:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Habit record already exists for this date"
        )

    # -----------------------------------------------------
    # 3. Create PostgreSQL record
    # -----------------------------------------------------

    record = HabitRecord(
        habit_id=habit_id,
        record_date=record_data.record_date,
        quantity=record_data.quantity
    )

    # -----------------------------------------------------
    # 4. Create Pixela Pixel
    # -----------------------------------------------------

    pixela_service = PixelaService()

    pixela_service.create_pixel(
        graph_id=habit.pixela_graph_id,
        record_date=record_data.record_date.strftime("%Y%m%d"),
        quantity=str(record_data.quantity)
    )

    # -----------------------------------------------------
    # 5. Save record in PostgreSQL
    # -----------------------------------------------------

    db.add(record)

    db.commit()

    db.refresh(record)

    return record


# ---------------------------------------------------------
# Get All Records
# ---------------------------------------------------------

def get_records(
    db: Session,
    habit_id: int,
    user_id: int
) -> list[HabitRecord]:

    # Make sure the habit belongs to the logged-in user
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

    return (
        db.query(HabitRecord)
        .filter(
            HabitRecord.habit_id == habit_id
        )
        .order_by(
            HabitRecord.record_date.desc()
        )
        .all()
    )


# ---------------------------------------------------------
# Get One Record
# ---------------------------------------------------------

def get_record(
    db: Session,
    habit_id: int,
    record_date: date,
    user_id: int
) -> HabitRecord | None:

    # Make sure the habit belongs to the logged-in user
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

    return (
        db.query(HabitRecord)
        .filter(
            HabitRecord.habit_id == habit_id,
            HabitRecord.record_date == record_date
        )
        .first()
    )


# ---------------------------------------------------------
# Update Record
# ---------------------------------------------------------

def update_record(
    db: Session,
    record: HabitRecord,
    record_data: HabitRecordUpdate
) -> HabitRecord:

    # Get the associated habit
    habit = (
        db.query(Habit)
        .filter(
            Habit.id == record.habit_id
        )
        .first()
    )

    if not habit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    # Update Pixela first
    pixela_service = PixelaService()

    pixela_service.update_pixel(
        graph_id=habit.pixela_graph_id,
        record_date=record.record_date.strftime("%Y%m%d"),
        quantity=str(record_data.quantity)
    )

    # Update PostgreSQL
    record.quantity = record_data.quantity

    db.commit()
    db.refresh(record)

    return record


# ---------------------------------------------------------
# Delete Record
# ---------------------------------------------------------

def delete_record(
    db: Session,
    record: HabitRecord
) -> None:

    # Get the habit associated with this record
    habit = (
        db.query(Habit)
        .filter(
            Habit.id == record.habit_id
        )
        .first()
    )

    if not habit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Habit not found"
        )

    # Delete pixel from Pixela
    pixela_service = PixelaService()

    pixela_service.delete_pixel(
        graph_id=habit.pixela_graph_id,
        record_date=record.record_date.strftime("%Y%m%d")
    )

    # Delete record from PostgreSQL
    db.delete(record)

    db.commit()