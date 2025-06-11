from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import user, finance

app = FastAPI(title="Finance Tracker App Backend")

# Allow CORS for frontend (adjust origins as needed)
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user.router, prefix="/api/user", tags=["user"])
app.include_router(finance.router, prefix="/api/finance", tags=["finance"])

@app.get("/")
async def root():
    return {"message": "Finance Tracker API is running"}
