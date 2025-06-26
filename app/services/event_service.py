from app.repositories import event_repository
from app.schemas import EventCreate, EventSearch
from sqlalchemy.orm import Session
from app.models import Event


def create_event_with_validation(event: EventCreate, db: Session) -> Event:
    eventModel = Event(**event.model_dump())
    return event_repository.save_event(eventModel, db)


def search_event(event_search: EventSearch, db: Session) -> list[Event]:
    filters = event_search.model_dump(exclude_unset=True)
    return event_repository.search_events(db, **filters)
