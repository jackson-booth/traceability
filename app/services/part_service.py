from sqlalchemy.orm import Session
from app.exceptions import PartNotFoundError
from app.schemas import EventRead, PartWithEvents
from app.repositories import event_repository


def get_part_events(part_serial: str, db: Session) -> PartWithEvents:
    """
    Retrieves all events for a specific part, ordered by timestamp.

    Args:
        part_serial (str): The serial number of the part.
        db (Session): The database session.

    Returns:
        dict: A dictionary containing the part serial and a list of events.

    Raises:
        HTTPException: If no events are found for the part.
    """
    events = event_repository.get_part_events(part_serial, db)

    if not events:
        raise PartNotFoundError(part_serial=part_serial)

    event_schemas = [EventRead.model_validate(event) for event in events]
    return PartWithEvents(part_serial=part_serial, events=event_schemas)
