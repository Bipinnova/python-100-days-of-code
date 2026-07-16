from pydantic import BaseModel


class OrderRequest(BaseModel):

    drink_name: str
    amount: int


class CoffeeResponse(BaseModel):

    success: bool
    message: str
    change: int