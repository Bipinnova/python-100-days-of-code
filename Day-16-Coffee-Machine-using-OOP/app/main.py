from fastapi import FastAPI, HTTPException

from app.schemas.coffee import OrderRequest
from app.services.coffee_service import coffee_service

app = FastAPI(
    title="Coffee Machine API",
    version="1.0.0"
)


@app.get("/", include_in_schema=False)
def home():

    return {
        "message": "Coffee Machine API"
    }


@app.get("/menu")
def menu():

    return {
        "available_drinks": coffee_service.get_menu()
    }


@app.get("/report")
def report():

    return coffee_service.report()


@app.post("/order")
def order(request: OrderRequest):

    result = coffee_service.order(
        drink_name=request.drink_name,
        amount=request.amount
    )

    if not result["success"]:
        raise HTTPException(
            status_code=400,
            detail=result
        )

    return result