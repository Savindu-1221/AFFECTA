from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import upload
from app.api import analyze
from app.api import auth
from app.db.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize app
app = FastAPI()

# ✅ Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Use frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(upload.router)
app.include_router(analyze.router)
app.include_router(auth.router)