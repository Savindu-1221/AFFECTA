from deepface import DeepFace
import cv2

def analyze_face_emotions(frames):
    """
    Analyze list of frames to detect dominant emotions using DeepFace.

    Args:
        frames (list): List of (index, frame) tuples from extract_frames()

    Returns:
        List of dicts with 'timestamp', 'dominant_emotion', and 'emotion_scores'
    """
    results = []
    for idx, frame in frames:
        try:
            # DeepFace returns a list of predictions
            analysis = DeepFace.analyze(frame, actions=["emotion"], enforce_detection=False)[0]

            result = {
                "timestamp": idx / 30,  # assuming 30fps
                "dominant_emotion": analysis["dominant_emotion"],
                "emotion_scores": analysis["emotion"]
            }
            results.append(result)
        except Exception as e:
            print(f"Frame {idx} could not be analyzed: {e}")

    print(f"[INFO] Analysis completed. Total frames analyzed: {len(results)}")
    return results
