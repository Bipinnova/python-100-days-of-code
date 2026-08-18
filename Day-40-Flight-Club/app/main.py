from fastapi import FastAPI

from app.routers.flights import router as flight_router
from app.routers.customers import router as customer_router
from app.routers.deals import router as deal_router


app = FastAPI(
    title="Flight Club API",
    description="Flight price tracking and notification API",
    version="1.0.0"
)


app.include_router(
    flight_router
)

app.include_router(
    customer_router
)

app.include_router(
    deal_router
)


@app.get("/", include_in_schema=False)
def home():

    return {
        "message": "Flight Club API is running"
    }