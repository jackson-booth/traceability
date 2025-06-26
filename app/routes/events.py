from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas
from app.services import event_service

router = APIRouter(
    prefix="/events",
    tags=["events"],
)


@router.post("/", response_model=schemas.EventRead)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    return event_service.create_event_with_validation(event, db)


@router.post("/search", response_model=List[schemas.EventRead])
def search_event(event_search: schemas.EventSearch, db: Session = Depends(get_db)):
    return event_service.search_event(event_search, db)
