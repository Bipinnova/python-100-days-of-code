from pydantic import BaseModel, Field


class ExerciseRequest(BaseModel):
    exercise_text: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Exercise description, maximum 50 characters"
    )


class ExerciseResponse(BaseModel):
    exercise: str
    duration: float
    calories: float