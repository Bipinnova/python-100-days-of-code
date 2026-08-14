from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class HabitUnit(str, Enum):
    MINUTES = "minutes"
    HOURS = "hours"
    PAGES = "pages"
    KILOMETERS = "kilometers"
    TIMES = "times"
    REPS = "reps"
    LITERS = "liters"


class HabitDataType(str, Enum):
    WHOLE_NUMBER = "whole_number"
    DECIMAL = "decimal"


class HabitColor(str, Enum):
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    RED = "red"
    YELLOW = "yellow"


class HabitCreate(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=100
    )

    description: str | None = Field(
        default=None,
        max_length=255
    )

    unit: HabitUnit

    data_type: HabitDataType

    color: HabitColor


class HabitUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    description: str | None = Field(
        default=None,
        max_length=255
    )

    unit: HabitUnit | None = None

    data_type: HabitDataType | None = None

    color: HabitColor | None = None


class HabitResponse(BaseModel):
    id: int
    user_id: int
    name: str
    description: str | None
    unit: str
    data_type: str
    color: str
    pixela_graph_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True