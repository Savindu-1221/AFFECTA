from sqlalchemy import Column, Integer, String, Date
from app.db.database import Base

class Session(Base):
    __tablename__ = "sessions"

    session_id = Column(Integer, primary_key=True, index=True)
    therapist_id = Column(Integer)
    patient_id = Column(Integer)
    session_date = Column(Date)
    video_file_path = Column(String)
    duration = Column(Integer)
