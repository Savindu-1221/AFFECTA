from fastapi import APIRouter, HTTPException
from app.db.database import SessionLocal
from app.models.session import Session
from app.models.emotion_analysis import EmotionAnalysis
from app.utils.cloud_storage import download_from_gdrive
from app.utils.video_processing import extract_frames, extract_audio
from app.utils.fer_model import analyze_face_emotions
from app.utils.ver_model import extract_audio_features, predict_emotion
import os

router = APIRouter()

@router.get("/analyze-session/{session_id}")
async def analyze_session(session_id: int):
    db = SessionLocal()
    try:
        # 1. Load session metadata
        session = db.query(Session).filter(Session.session_id == session_id).first()
        if not session:
            raise HTTPException(status_code=404, detail="Session not found")

        # 2. Download video from Google Drive
        video_url = session.video_file_path
        file_id = video_url.split("/d/")[1].split("/")[0]
        local_path = f"temp_session_{session_id}.mp4"
        download_from_gdrive(file_id, local_path)

        # 3. Run FER
        frames = extract_frames(local_path)
        fer_results = analyze_face_emotions(frames)

        # Convert np.float32 values to float for JSON compatibility
        for item in fer_results:
            item["emotion_scores"] = {k: float(v) for k, v in item["emotion_scores"].items()}

        # 4. Run VER
        audio_path = extract_audio(local_path, f"{local_path}.wav")
        features = extract_audio_features(audio_path)
        ver_emotion = predict_emotion(features)

        # 5. Save FER results to database
        for item in fer_results:
            db.add(EmotionAnalysis(
                session_id=session_id,
                timestamp=item["timestamp"],
                dominant_emotion=item["dominant_emotion"],
                emotion_scores=item["emotion_scores"]
            ))

        # 6. Save VER result to database (timestamp = -1 means entire audio)
        db.add(EmotionAnalysis(
            session_id=session_id,
            timestamp=-1,
            dominant_emotion=ver_emotion,
            emotion_scores={}
        ))

        db.commit()

        # 7. Cleanup
        try:
            os.remove(local_path)
            os.remove(audio_path)
        except Exception as cleanup_err:
            print(f"[WARN] Cleanup failed: {cleanup_err}")

        return {
            "status": "analyzed",
            "session_id": session_id,
            "FER_results": fer_results,
            "VER_result": ver_emotion
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
    finally:
        db.close()