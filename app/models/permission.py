from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Enum as sqlEnum
from ..Database.db import Base
from enum import Enum


class Permission_Project_Enum(str, Enum):
    create_project = "create_project"
    delete_user = "delete_user"


class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[Permission_Project_Enum] = mapped_column(
        sqlEnum[Permission_Project_Enum], nullable=False, unique=True, index=True
    )
    description: Mapped[str] = mapped_column(String(255), nullable=False)
