from typing import List
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
