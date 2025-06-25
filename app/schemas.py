from pydantic import BaseModel, Field
from typing import Literal, Optional, List
from datetime import datetime
import uuid
from app.models import EventType


class EventCreate(BaseModel):
    part_serial: str
    event_type: EventType
    station_id: Optional[str]
    timestamp: datetime
    user_id: Optional[str]
    payload: dict


class EventRead(EventCreate):
    id: uuid.UUID
    created_at: datetime

class PartEventsRead(BaseModel):
    part_serial: str
    events: List[EventRead]