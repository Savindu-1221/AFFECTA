from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.db.database import SessionLocal
from app.models.session import Session
from app.utils.cloud_storage import upload_to_gdrive
import uuid, os
from datetime import datetime

router = APIRouter()

@router.post("/upload-video")
async def upload_video(
    therapist_id: int = Form(...),
    patient_id: int = Form(...),
    session_date: str = Form(...),
    file: UploadFile = File(...)
):
    try:
        # === Step 1: Save uploaded file to disk ===
        file_ext = file.filename.split(".")[-1]
        file_key = f"{uuid.uuid4()}.{file_ext}"
        temp_path = f"temp_{file_key}"

        # Save file to disk and fully close it
        with open(temp_path, "wb") as buffer:
            buffer.write(await file.read())

        # === Step 2: Open clean file handle for upload ===
        with open(temp_path, "rb") as f:
            file_id = upload_to_gdrive(f, file_key)

        video_url = f"https://drive.google.com/file/d/{file_id}/view"

        # === Step 3: Save session metadata to DB ===
        db = SessionLocal()
        new_session = Session(
            therapist_id=therapist_id,
            patient_id=patient_id,
            session_date=datetime.strptime(session_date, "%Y-%m-%d").date(),
            video_file_path=video_url,
            duration=0
        )
        db.add(new_session)
        db.commit()
        db.refresh(new_session)
        db.close()

        # === Step 4: Remove temp file safely ===
        try:
            os.remove(temp_path)
        except Exception as cleanup_err:
            print(f"[WARN] Could not delete file: {cleanup_err}")

        return {
            "status": "uploaded",
            "session_id": new_session.session_id,
            "video_url": video_url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")
