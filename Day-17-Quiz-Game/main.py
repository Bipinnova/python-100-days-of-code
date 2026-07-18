from fastapi import FastAPI

from app.api.quiz import router as quiz_router

app = FastAPI(
    title="Quiz Game API",
    version="1.0.0"
)

app.include_router(quiz_router)