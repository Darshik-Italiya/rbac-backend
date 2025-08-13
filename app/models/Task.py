from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (
    Integer,
    String,
    Enum as sqlEnum,
    ForeignKey,
    DateTime,
    func,
    Date,
)
from datetime import datetime, date
from enum import Enum
from ..Database.db import Base


class Task_Status_Enum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("projects.id"))
    assigned_to: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    title: Mapped[str] = mapped_column(String, nullable=False, index=True)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[Task_Status_Enum] = mapped_column(
        sqlEnum(Task_Status_Enum), nullable=False, unique=True, index=True
    )

    due_date: Mapped[date] = mapped_column(Date, default=date.today)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
