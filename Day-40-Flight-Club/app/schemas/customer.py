from pydantic import BaseModel, EmailStr, Field


class CustomerCreate(BaseModel):

    first_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    last_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    email: EmailStr

    phone: str | None = Field(
        default=None,
        max_length=20
    )


class CustomerUpdate(BaseModel):

    first_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    last_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    email: EmailStr | None = None

    phone: str | None = Field(
        default=None,
        max_length=20
    )

    is_active: bool | None = None


class CustomerResponse(BaseModel):

    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None
    is_active: bool

    class Config:
        from_attributes = True