from sqlalchemy import Column, Integer, String, Float, Text
from app.models.base import Base

class Tender(Base):
    __tablename__ = "tenders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    budget = Column(Float)
    deadline = Column(String)
    source_url = Column(String)
