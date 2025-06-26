from pydantic import BaseModel
from typing import Any, Optional, List
from datetime import datetime
import uuid
from app.models import EventType


class BaseSchema(BaseModel):
    class Config:
        from_attributes = True


class EventCreate(BaseSchema):
    part_serial: str
    event_type: EventType
    station_id: Optional[str]
    timestamp: datetime
    user_id: Optional[str]
    payload: dict[str, Any]


class EventRead(EventCreate):
    id: uuid.UUID
    created_at: datetime


class PartEventsRead(BaseSchema):
    part_serial: str
    events: List[EventRead]


class PartWithEvents(BaseSchema):
    part_serial: str
    events: List[EventRead]


class EventSearch(BaseSchema):
    part_serial: Optional[str] = None
    event_type: Optional[EventType] = None
    station_id: Optional[str] = None
    user_id: Optional[str] = None
    start_timestamp: Optional[datetime] = None
    end_timestamp: Optional[datetime] = None
