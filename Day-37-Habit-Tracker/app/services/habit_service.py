import hashlib
import re

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.habit import Habit
from app.schemas.habit import HabitCreate, HabitUpdate
from app.services.pixela_service import PixelaService


# =========================================================
# Pixela Graph ID
# =========================================================

def generate_pixela_graph_id(
    user_id: int,
    habit_name: str
) -> str:
    """
    Generate a valid Pixela graph ID.

    Pixela format:
    [a-z][a-z0-9-]{1,16}

    Example:
        User 1
        Coding Practice

        u1-coding-c2ed
    """

    # Convert name to lowercase
    clean_name = habit_name.lower().strip()

    # Replace spaces/special characters with "-"
    clean_name = re.sub(
        r"[^a-z0-9]+",
        "-",
        clean_name
    )

    # Remove leading/trailing "-"
    clean_name = clean_name.strip("-")

    # Create a short hash
    hash_value = hashlib.sha1(
        f"{user_id}-{habit_name.lower()}".encode("utf-8")
    ).hexdigest()[:4]

    # Keep name short enough
    clean_name = clean_name[:7].rstrip("-")

    # Final format:
    # u1-coding-c2ed
    graph_id = f"u{user_id}-{clean_name}-{hash_value}"

    # Final safety cleanup
    graph_id = re.sub(
        r"[^a-z0-9-]",
        "-",
        graph_id
    )

    # Maximum 17 characters
    graph_id = graph_id[:17].rstrip("-")

    return graph_id


# =========================================================
# Create Habit
# =========================================================

def create_habit(
    db: Session,
    user_id: int,
    habit_data: HabitCreate
) -> Habit:

    # -----------------------------------------------------
    # Check duplicate habit name
    # -----------------------------------------------------

    existing_habit = (
        db.query(Habit)
        .filter(
            Habit.user_id == user_id,
            Habit.name == habit_data.name
        )
        .first()
    )

    if existing_habit:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Habit with this name already exists"
        )

    # -----------------------------------------------------
    # Generate Pixela graph ID
    # -----------------------------------------------------

    graph_id = generate_pixela_graph_id(
        user_id=user_id,
        habit_name=habit_data.name
    )

    # -----------------------------------------------------
    # Create Pixela graph
    # -----------------------------------------------------

    print("Generated Pixela graph ID:", repr(graph_id))
    print("Graph ID length:", len(graph_id))
    
    pixela_service = PixelaService()

    try:
        pixela_service.create_graph(
            graph_id=graph_id,
            name=habit_data.name,
            unit=habit_data.unit.value,
            data_type=habit_data.data_type.value,
            color=habit_data.color.value
        )

    except Exception as exc:

        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Unable to create Pixela graph: {str(exc)}"
        )

    # -----------------------------------------------------
    # Create Habit in PostgreSQL
    # -----------------------------------------------------

    habit = Habit(
        user_id=user_id,
        name=habit_data.name,
        description=habit_data.description,
        unit=habit_data.unit.value,
        data_type=habit_data.data_type.value,
        color=habit_data.color.value,
        pixela_graph_id=graph_id
    )

    try:

        db.add(habit)
        db.commit()
        db.refresh(habit)

    except Exception:

        db.rollback()

        # -------------------------------------------------
        # PostgreSQL failed after Pixela graph succeeded.
        #
        # Try to remove the orphan Pixela graph.
        # -------------------------------------------------

        try:
            pixela_service.delete_graph(
                graph_id=graph_id
            )
        except Exception:
            pass

        raise

    return habit


# =========================================================
# Get All Habits
# =========================================================

def get_user_habits(
    db: Session,
    user_id: int
) -> list[Habit]:

    habits = (
        db.query(Habit)
        .filter(
            Habit.user_id == user_id
        )
        .order_by(
            Habit.created_at.desc()
        )
        .all()
    )

    return habits


# =========================================================
# Get One Habit
# =========================================================

def get_habit(
    db: Session,
    habit_id: int,
    user_id: int
) -> Habit:

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

    return habit


# =========================================================
# Update Habit
# =========================================================

def update_habit(
    db: Session,
    habit_id: int,
    user_id: int,
    habit_data: HabitUpdate
) -> Habit:

    # -----------------------------------------------------
    # Get user's habit
    # -----------------------------------------------------

    habit = get_habit(
        db=db,
        habit_id=habit_id,
        user_id=user_id
    )

    # -----------------------------------------------------
    # Get only fields sent by user
    # -----------------------------------------------------

    update_data = habit_data.model_dump(
        exclude_unset=True
    )

    # -----------------------------------------------------
    # Convert Enum values to strings
    # -----------------------------------------------------

    if "unit" in update_data:

        update_data["unit"] = (
            update_data["unit"].value
        )

    if "data_type" in update_data:

        update_data["data_type"] = (
            update_data["data_type"].value
        )

    if "color" in update_data:

        update_data["color"] = (
            update_data["color"].value
        )

    # -----------------------------------------------------
    # Check duplicate habit name
    # -----------------------------------------------------

    if "name" in update_data:

        existing_habit = (
            db.query(Habit)
            .filter(
                Habit.user_id == user_id,
                Habit.name == update_data["name"],
                Habit.id != habit_id
            )
            .first()
        )

        if existing_habit:

            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Habit with this name already exists"
            )

    # -----------------------------------------------------
    # Update PostgreSQL habit
    # -----------------------------------------------------

    for field, value in update_data.items():

        setattr(
            habit,
            field,
            value
        )

    db.commit()
    db.refresh(habit)

    return habit


# =========================================================
# Delete Habit
# =========================================================

def delete_habit(
    db: Session,
    habit_id: int,
    user_id: int
) -> None:

    # -----------------------------------------------------
    # Get user's habit
    # -----------------------------------------------------

    habit = get_habit(
        db=db,
        habit_id=habit_id,
        user_id=user_id
    )

    # -----------------------------------------------------
    # Save Pixela graph ID before deleting DB record
    # -----------------------------------------------------

    graph_id = habit.pixela_graph_id

    pixela_service = PixelaService()

    # -----------------------------------------------------
    # Delete Pixela graph first
    # -----------------------------------------------------

    try:

        pixela_service.delete_graph(
            graph_id=graph_id
        )

    except Exception as exc:

        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Unable to delete Pixela graph: {str(exc)}"
        )

    # -----------------------------------------------------
    # Delete Habit from PostgreSQL
    # -----------------------------------------------------

    db.delete(habit)
    db.commit()