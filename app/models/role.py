from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, func, Enum as sqlEnum
from enum import Enum
from datetime import datetime
from ..Database.db import Base


class Role_Enum(str, Enum):
    admin = "admin"
    manager = "manager"
    employee = "employee"


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[Role_Enum] = mapped_column(
        sqlEnum[Role_Enum], nullable=False, unique=True, index=True
    )
    description: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
