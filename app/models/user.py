from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, ForeignKey, func, DateTime
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from ..Database.db import Base


class User(Base):
    __tablename__ = "users"

    # ID using UUID
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )

    # Role ID
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("roles.id"))

    username: Mapped[str] = mapped_column(
        String, unique=True, index=True, nullable=False
    )
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), onupdate=func.now(), server_default=func.now()
    )
