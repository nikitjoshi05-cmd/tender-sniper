from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.models.company import CompanyProfile as CompanyProfileModel
from app.schemas.company_schema import CompanyProfileCreate, CompanyProfile

router = APIRouter()

@router.post("/", response_model=CompanyProfile)
def create_company(company: CompanyProfileCreate, db: Session = Depends(get_db)):
    db_company = CompanyProfileModel(**company.model_dump())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@router.get("/", response_model=List[CompanyProfile])
def get_companies(db: Session = Depends(get_db)):
    return db.query(CompanyProfileModel).all()
