from pydantic import BaseModel, EmailStr, Field, SecretStr


class UserCreate(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50
    )

    email: EmailStr

    password: SecretStr = Field(
        min_length=8,
        max_length=100
    )


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str