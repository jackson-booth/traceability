from typing import List, Optional
from app import models
from sqlalchemy.orm import Session


def save_event(event: models.Event, db: Session) -> models.Event:
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def get_part_events(part_serial: str, db: Session) -> List[models.Event]:
    """
    Retrieves all events for a specific part, ordered by timestamp.

    Args:
        part_serial (str): The serial number of the part.
        db (Session): The database session.

    Returns:
        List[models.Event]: A list of events associated with the part, ordered by timestamp.

    Raises:
        HTTPException: If no events are found for the part.
    """
    return (
        db.query(models.Event)
        .filter(models.Event.part_serial == part_serial)
        .order_by(models.Event.timestamp.asc())
        .all()
    )


def search_events(
    db: Session,
    part_serial: Optional[str] = None,
    event_type: Optional[str] = None,
    station_id: Optional[str] = None,
    user_id: Optional[str] = None,
    start_timestamp: Optional[str] = None,
    end_timestamp: Optional[str] = None,
) -> List[models.Event]:
    """Searches for events based on various filters."""
    query = db.query(models.Event)

    if part_serial:
        query = query.filter(models.Event.part_serial == part_serial)
    if event_type:
        query = query.filter(models.Event.event_type == event_type)
    if station_id:
        query = query.filter(models.Event.station_id == station_id)
    if user_id:
        query = query.filter(models.Event.user_id == user_id)
    if start_timestamp:
        query = query.filter(models.Event.timestamp >= start_timestamp)
    if end_timestamp:
        query = query.filter(models.Event.timestamp <= end_timestamp)

    return query.order_by(models.Event.timestamp.asc()).all()
