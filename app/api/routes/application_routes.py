from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.models.application_log import ApplicationLog as ApplicationLogModel
from app.schemas.application_schema import ApplicationLog

router = APIRouter()

@router.get("/", response_model=List[ApplicationLog])
def get_applications(db: Session = Depends(get_db)):
    return db.query(ApplicationLogModel).all()
