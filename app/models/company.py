from sqlalchemy import Column, Integer, String, Float, JSON
from app.models.base import Base

class CompanyProfile(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    skills = Column(JSON)
    certifications = Column(JSON)
    min_budget = Column(Float)
    max_budget = Column(Float)
