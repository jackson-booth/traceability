from app.repositories import event_repository
from app.schemas import EventCreate
from sqlalchemy.orm import Session
from app.models import Event


def create_event_with_validation(event: EventCreate, db: Session) -> Event:
    eventModel = Event(**event.dict())
    return event_repository.save_event(eventModel, db)
