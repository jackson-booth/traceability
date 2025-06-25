from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.services import event_service

router = APIRouter(
    prefix="/events",
    tags=["events"],
)


@router.post("/", response_model=schemas.EventRead)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return event_service.create_event_with_validation(event, db)
