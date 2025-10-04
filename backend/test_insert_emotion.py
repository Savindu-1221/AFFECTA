from app.db.database import SessionLocal
from app.models.emotion_analysis import EmotionAnalysis

# Create a database session
db = SessionLocal()

# Create a fake test emotion analysis record
test_emotion = EmotionAnalysis(
    session_id=1,  # 👈 Assume session ID 1 exists. (Otherwise adjust)
    timestamp=5.0,  # 5 seconds into video
    dominant_emotion="happy",
    emotion_scores={
        "angry": 0.02,
        "happy": 0.85,
        "sad": 0.05,
        "neutral": 0.07,
        "surprise": 0.01
    }
)

# Insert into database
db.add(test_emotion)
db.commit()
db.refresh(test_emotion)

print(f"Inserted test emotion analysis with ID: {test_emotion.id}")

# Close the database session
db.close()
