from pydantic import BaseModel
from typing import List

class CompanyProfileBase(BaseModel):
    name: str
    skills: List[str]
    certifications: List[str]
    min_budget: float
    max_budget: float

class CompanyProfileCreate(CompanyProfileBase):
    pass

class CompanyProfile(CompanyProfileBase):
    id: int

    class Config:
        from_attributes = True
