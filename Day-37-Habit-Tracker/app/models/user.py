from datetime import datetime

from sqlalchemy import Boolean, String, func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    # created_at: Mapped[datetime] = mapped_column(
    #     DateTime,
    #     default=datetime.utcnow
    # )
    
    created_at: Mapped[datetime] = mapped_column(
    TIMESTAMP(precision=0),
    server_default=func.now(),
    nullable=False
    )