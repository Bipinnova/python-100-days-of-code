from fastapi import FastAPI, HTTPException

from app.schemas import ExerciseRequest
from app.services.exercise_service import get_exercises
from app.services.sheet_service import save_exercise


app = FastAPI(
    title="Exercise Tracker API",
    description="Exercise Tracker using FastAPI, Exercise API and Sheety",
    version="1.0.0",
)


@app.get("/", include_in_schema=False)
def root():
    return {
        "message": "Exercise Tracker API is running"
    }


@app.post("/exercise")
def track_exercise(request: ExerciseRequest):

    try:
        exercises = get_exercises(
            request.exercise_text
        )

        saved_exercises = []

        for exercise in exercises:

            sheet_response = save_exercise(exercise)

            saved_exercises.append({
                "exercise": exercise["name"],
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
                "sheet_response": sheet_response,
            })

        return {
            "message": "Exercise tracked successfully",
            "data": saved_exercises,
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Something went wrong: {str(exc)}"
        )