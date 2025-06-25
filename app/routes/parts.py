from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.exceptions import PartNotFoundError
from app.services import part_service

router = APIRouter(
    prefix="/parts",
    tags=["parts"],
)


@router.get("/{part_serial}/events", response_model=schemas.PartEventsRead)
def get_part_events(part_serial: str, db: Session = Depends(get_db)):
    return part_service.get_part_events(part_serial, db=db)
