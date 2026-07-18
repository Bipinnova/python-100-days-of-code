from fastapi import APIRouter
from app.schemas.quiz_schema import SubmitAnswerRequest

from app.services.quiz_service import (
    get_questions,
    check_answer
)

router = APIRouter()

@router.get("/qiuz")
async def root():
    return get_questions()


@router.post("/submit")
def submit_answer(request: SubmitAnswerRequest):
    return check_answer(request)