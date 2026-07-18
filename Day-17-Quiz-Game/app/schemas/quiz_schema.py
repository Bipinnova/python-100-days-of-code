from pydantic import BaseModel

class SubmitAnswerRequest(BaseModel):
    question_id: int
    selected_answer: str
    