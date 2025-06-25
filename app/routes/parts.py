from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/parts",
    tags=["parts"],
)

@router.get("/{part_serial}/events", response_model=schemas.PartEventsRead)
def get_part_events(part_serial: str, db: Session = Depends(get_db)):
    db_events = db.query(models.Event).filter(models.Event.part_serial == part_serial).order_by(models.Event.timestamp.asc()).all()
    if not db_events:
        raise HTTPException(status_code=404, detail="Part not found or no events recorded for this part")
  
    return { "part_serial": part_serial, "events": db_events}
