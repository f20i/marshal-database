from __future__ import annotations
from typing import TYPE_CHECKING

import uuid

from sqlalchemy import ForeignKey, String, text, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class Device(Base):
    __tablename__ = "Device"
    __table_args__ = {"schema": "marshal"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    serial: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String, nullable=False, default="waiting")
    meta: Mapped[dict] = mapped_column(
        "metadata",
        JSONB,
        nullable=False,
        server_default=text("'{}'::jsonb"),
        default=dict,
    )

    def __repr__(self):
        return f"""
    Device(id={self.id},
    serial={self.serial},
    name={self.name},
    description={self.description},
    status={self.status},
    meta={self.meta}
    created_at={self.created_at}
    updated_at={self.updated_at}
    deleted_at={self.deleted_at}
"""
