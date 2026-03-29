from pydantic import BaseModel

class TenderBase(BaseModel):
    title: str
    description: str
    budget: float
    deadline: str
    source_url: str

class Tender(TenderBase):
    id: int

    class Config:
        from_attributes = True
