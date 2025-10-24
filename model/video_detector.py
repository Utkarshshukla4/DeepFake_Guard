import cv2
import numpy as np
from deepface import DeepFace

def detect_fake_frame(frame):
    try:
        analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if analysis and 'dominant_emotion' in analysis[0]:
            # Simple rule: inconsistent emotion frames over time → potential fake
            return False
        else:
            return True
    except Exception:
        return True
