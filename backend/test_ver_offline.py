from app.utils.ver_model import extract_audio_features, predict_emotion
from app.utils.video_processing import extract_audio
import os

# === CONFIGURATION ===
video_path = "Test.mp4"  # Path to the input video file
audio_output_path = "sample_audio.wav"

# === STEP 1: Extract audio from video ===
print("[INFO] Extracting audio from video...")
if not os.path.exists(video_path):
    print(f"[ERROR] Video file '{video_path}' not found!")
    exit()

audio_path = extract_audio(video_path, audio_output_path)
print(f"[INFO] Audio extracted to: {audio_path}")

# === STEP 2: Extract audio features ===
print("[INFO] Extracting audio features...")
features = extract_audio_features(audio_path)

if features is not None:
    print("[INFO] Audio features extracted!")
    
    # === STEP 3: Predict emotion ===
    emotion = predict_emotion(features)
    print(f"[RESULT] Predicted voice emotion: {emotion}")
else:
    print("[ERROR] Failed to extract audio features.")
