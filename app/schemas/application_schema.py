from pydantic import BaseModel
from datetime import datetime

class ApplicationLogBase(BaseModel):
    status: str
    applied_at: datetime
    tender_id: int

class ApplicationLog(ApplicationLogBase):
    id: int

    class Config:
        from_attributes = True
