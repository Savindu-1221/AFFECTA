import librosa
import numpy as np

def extract_audio_features(audio_path):
    """
    Extract MFCC and Chroma features from an audio file.
    
    Args:
        audio_path (str): Path to the audio (.wav) file.

    Returns:
        feature_vector (np.array): Combined feature vector.
    """
    try:
        y, sr = librosa.load(audio_path, sr=None)

        # Extract MFCC features
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfcc_mean = np.mean(mfcc, axis=1)

        # Extract Chroma features
        chroma = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_mean = np.mean(chroma, axis=1)

        # Combine MFCC and Chroma into one feature vector
        feature_vector = np.concatenate((mfcc_mean, chroma_mean))

        return feature_vector

    except Exception as e:
        print(f"Error extracting features: {e}")
        return None

def predict_emotion(feature_vector):
    
    if feature_vector is None:
        return "unknown"

    energy = np.mean(feature_vector)

    if energy > 0:
        return "happy"
    else:
        return "neutral"
