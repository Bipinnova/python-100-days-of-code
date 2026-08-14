from fastapi import FastAPI

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.habits import router as habits_router
from app.routers.records import router as records_router
from app.routers.stats import router as stats_router
from app.routers.dashboard import router as dashboard_router

app = FastAPI(
    title="Habit Tracker API",
    description=(
        "Habit Tracker API built with FastAPI, "
        "PostgreSQL, SQLAlchemy and Pixela"
    ),
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(habits_router)
app.include_router(records_router)
app.include_router(stats_router)
app.include_router(dashboard_router)