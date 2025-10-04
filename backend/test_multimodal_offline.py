from app.utils.video_processing import extract_frames, extract_audio
from app.utils.fer_model import analyze_face_emotions
from app.utils.ver_model import extract_audio_features, predict_emotion
import os

# === CONFIG ===
video_path = "Test.mp4"          # 👈 Make sure this video exists
audio_output_path = "sample_audio.wav" # Temp file for voice analysis

# === STEP 1: Check video ===
if not os.path.exists(video_path):
    print(f"[ERROR] Video file '{video_path}' not found!")
    exit()

# === STEP 2: Extract frames (for FER) ===
print("[INFO] Extracting video frames for FER...")
frames = extract_frames(video_path, frame_interval=30)  # approx. 1 per sec
print(f"[INFO] Total frames extracted: {len(frames)}")

# === STEP 3: Analyze frames (FER) ===
print("[INFO] Running face emotion recognition...")
fer_results = analyze_face_emotions(frames)
print(f"[INFO] FER complete. Total analyzed frames: {len(fer_results)}\n")

# === STEP 4: Extract audio from video (for VER) ===
print("[INFO] Extracting audio from video...")
audio_path = extract_audio(video_path, audio_output_path)
print(f"[INFO] Audio saved to: {audio_path}")

# === STEP 5: Analyze audio (VER) ===
print("[INFO] Running voice emotion recognition...")
features = extract_audio_features(audio_path)
voice_emotion = predict_emotion(features)
print("[INFO] VER complete.\n")

# === DISPLAY RESULTS ===
print("========== AFFECTA EMOTION ANALYSIS ==========\n")

print("🎭 Face Emotion Recognition (FER):")
for item in fer_results:
    ts = item["timestamp"]
    emo = item["dominant_emotion"]
    print(f"  • Time {ts:.1f}s → {emo}")

print("\n🎤 Voice Emotion Recognition (VER):")
print(f"  • Overall Voice Emotion: {voice_emotion}")

print("\n===============================================")
