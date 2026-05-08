from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class DeviceSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    serial: str
    name: str
    description: str | None = None
    status: str = Field(default="waiting")
    metadata: dict = Field(default_factory=dict, alias="meta")
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None


DeviceSchema.model_rebuild()