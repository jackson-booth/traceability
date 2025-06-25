from sqlalchemy import Column, String, Enum, JSON, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import enum
import uuid

from app.database import Base


class EventType(str, enum.Enum):
    part_created = "part_created"
    inspection_passed = "inspection_passed"
    inspection_failed = "inspection_failed"
    rework_done = "rework_done"
    part_moved = "part_moved"
    defect_found = "defect_found"
    shipped = "shipped"


class Event(Base):
    __tablename__ = "events"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    part_serial = Column(String, nullable=False)
    event_type = Column(Enum(EventType), nullable=False)
    station_id = Column(String)
    timestamp = Column(TIMESTAMP(timezone=True), nullable=False)
    user_id = Column(String)
    payload = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
