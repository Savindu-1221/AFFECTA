from fastapi import APIRouter, HTTPException, Depends, Form
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.therapist import Therapist
from app.utils.auth import hash_password, verify_password

router = APIRouter()

@router.post("/register")
def register(name: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    if db.query(Therapist).filter(Therapist.email == email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_therapist = Therapist(
        name=name,
        email=email,
        hashed_password=hash_password(password)
    )
    db.add(new_therapist)
    db.commit()
    return {"message": "Registration successful"}

@router.post("/login")
def login(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(Therapist).filter(Therapist.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "therapist_id": user.id}
