from app.utils.fer_model import analyze_face_emotions
import pprint

# --- SET YOUR TEST VIDEO PATH BELOW ---
test_video_path = "Test.mp4"  # 👈 put your video file name here (must be in backend folder)

# --- Analyze Emotions ---
print("[INFO] Starting Face Emotion Recognition...")

results = analyze_face_emotions(test_video_path, frame_interval=30)

print(f"[INFO] Analysis completed. Total frames analyzed: {len(results)}")

# --- Pretty Print Results ---
pprint.pprint(results)
