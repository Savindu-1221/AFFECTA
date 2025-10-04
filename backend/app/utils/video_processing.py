import cv2
from moviepy.editor import VideoFileClip

def extract_frames(video_path, frame_interval=30):
    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            frames.append((frame_count, frame))
        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()
    return frames

def extract_audio(video_path, output_audio_path):
    clip = VideoFileClip(video_path)
    clip.audio.write_audiofile(output_audio_path)
    
    # 🔒 CLOSE handles properly
    clip.reader.close()
    if clip.audio:
        clip.audio.reader.close_proc()
    del clip

    return output_audio_path
