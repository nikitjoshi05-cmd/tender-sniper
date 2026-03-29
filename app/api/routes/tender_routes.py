from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.models.tender import Tender as TenderModel
from app.schemas.tender_schema import Tender

router = APIRouter()

@router.get("/", response_model=List[Tender])
def get_tenders(db: Session = Depends(get_db)):
    return db.query(TenderModel).all()
