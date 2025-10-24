import numpy as np
import librosa

def detect_fake_audio(audio_path):
    try:
        y, sr = librosa.load(audio_path)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        # Example heuristic: unnatural uniform MFCC variation → possible fake
        var = np.var(mfcc)
        return var < 50.0
    except Exception:
        return False
