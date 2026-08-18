from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.customer import Customer
from app.schemas.customer import (
    CustomerCreate,
    CustomerUpdate,
    CustomerResponse,
)


router = APIRouter(
    prefix="/api/v1/customers",
    tags=["Customers"]
)


@router.post(
    "",
    response_model=CustomerResponse,
    status_code=201
)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):

    existing_customer = (
        db.query(Customer)
        .filter(
            Customer.email == customer.email
        )
        .first()
    )

    if existing_customer:

        raise HTTPException(
            status_code=409,
            detail="Customer with this email already exists."
        )

    new_customer = Customer(
        first_name=customer.first_name,
        last_name=customer.last_name,
        email=customer.email,
        phone=customer.phone,
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


@router.get(
    "",
    response_model=list[CustomerResponse]
)
def get_customers(
    db: Session = Depends(get_db)
):

    customers = (
        db.query(Customer)
        .order_by(Customer.id)
        .all()
    )

    return customers


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse
)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = (
        db.query(Customer)
        .filter(
            Customer.id == customer_id
        )
        .first()
    )

    if not customer:

        raise HTTPException(
            status_code=404,
            detail="Customer not found."
        )

    return customer


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse
)
def update_customer(
    customer_id: int,
    customer_data: CustomerUpdate,
    db: Session = Depends(get_db)
):

    customer = (
        db.query(Customer)
        .filter(
            Customer.id == customer_id
        )
        .first()
    )

    if not customer:

        raise HTTPException(
            status_code=404,
            detail="Customer not found."
        )

    update_data = customer_data.model_dump(
        exclude_unset=True
    )

    if "email" in update_data:

        existing_email = (
            db.query(Customer)
            .filter(
                Customer.email
                == update_data["email"],
                Customer.id != customer_id
            )
            .first()
        )

        if existing_email:

            raise HTTPException(
                status_code=409,
                detail=(
                    "Another customer already "
                    "uses this email."
                )
            )

    for field, value in update_data.items():

        setattr(
            customer,
            field,
            value
        )

    db.commit()
    db.refresh(customer)

    return customer


@router.delete(
    "/{customer_id}"
)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = (
        db.query(Customer)
        .filter(
            Customer.id == customer_id
        )
        .first()
    )

    if not customer:

        raise HTTPException(
            status_code=404,
            detail="Customer not found."
        )

    db.delete(customer)
    db.commit()

    return {
        "message": "Customer deleted successfully.",
        "customer_id": customer_id
    }