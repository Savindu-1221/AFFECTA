from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Therapist(Base):
    __tablename__ = "therapists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
