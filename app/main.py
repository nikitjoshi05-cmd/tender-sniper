from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import company_routes, tender_routes, application_routes, agent_routes
from app.core.database import engine
from app.models.base import Base

# Import models so SQLAlchemy creates tables properly
from app.models.company import CompanyProfile
from app.models.tender import Tender
from app.models.application_log import ApplicationLog

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tender Sniper API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(company_routes.router, prefix="/company", tags=["Company"])
app.include_router(tender_routes.router, prefix="/tenders", tags=["Tenders"])
app.include_router(application_routes.router, prefix="/applications", tags=["Applications"])
app.include_router(agent_routes.router, prefix="/agent", tags=["Agent"])

@app.get("/")
def read_root():
    return "Tender Sniper Running 🚀"
