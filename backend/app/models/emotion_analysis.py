from sqlalchemy import Column, Integer, Float, String, ForeignKey, JSON
from app.db.database import Base

class EmotionAnalysis(Base):
    __tablename__ = "emotion_analysis"

    id = Column(Integer, primary_key=True, index=True)
    
    session_id = Column(Integer, ForeignKey("sessions.session_id"))
    timestamp = Column(Float)  # Seconds in the video
    dominant_emotion = Column(String)  # E.g., "happy", "sad", "angry"
    emotion_scores = Column(JSON)  # Full emotion scores as JSON
