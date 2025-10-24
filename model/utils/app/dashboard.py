import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
import streamlit as st
import cv2
from model.video_detector import detect_fake_frame

st.title("🧠 DF-Guard: Deepfake Detector")
st.write("Upload a video or use webcam to detect possible deepfakes.")

video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if video_file is not None:
    tfile = open("temp_video.mp4", "wb")
    tfile.write(video_file.read())

    cap = cv2.VideoCapture("temp_video.mp4")
    fake_count = 0
    total = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        total += 1
        if detect_fake_frame(frame):
            fake_count += 1

    cap.release()
    confidence = (fake_count / total) * 100
    st.metric("Fake Probability", f"{confidence:.2f}%")

elif st.button("Use Webcam"):
    st.write("Webcam mode coming soon (use main.py for live mode).")
