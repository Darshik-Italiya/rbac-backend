from sqlalchemy import Integer, String, DateTime, Enum as sqlEnum, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from enum import Enum
from ..Database.db import Base


class Project_Status(str, Enum):
    active = "active"
    complete = "complete"


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    # User ID
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[Project_Status] = mapped_column(
        sqlEnum(Project_Status), nullable=True, index=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )
