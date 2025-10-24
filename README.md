# 🧠 DF-Guard: Deepfake Detection System

**Developed by Utkarsh Shukla**

DF-Guard is an AI-powered cybersecurity project designed to **detect Deepfake videos and audio** using modern deep learning models.  
It provides a **Streamlit dashboard** for video analysis and live detection using your webcam.
---

## 🚀 Features

- 🎥 **Real-Time Deepfake Detection** – Analyze live webcam feed for fake faces.  
- 🔊 **Audio Forgery Detection** – Detect AI-generated or modified voices.  
- 🤖 **AI Model Integration** – Uses CNN and spectral feature analysis.  
- 🌐 **Streamlit Dashboard** – For video upload and visual analysis.  
- 🔐 **Cybersecurity Application** – Prevents media forgery and misinformation.

---


---

## ⚙️ Installation & Setup

## Activate the Virtual Environment
python -m venv env
env\Scripts\activate
## Install Project Dependencies
pip install -r requirements.txt
## Run the Project

Option 1: Live Detection (Webcam)

python main.py
Opens a live webcam window with “REAL” or “FAKE” overlay.
Press Q to exit.


Option 2: Streamlit Dashboard

streamlit run model/utils/app/dashboard.py
Opens a browser dashboard to upload a video for detection.
Shows the fake probability percentage.


Stop the Project
Press Ctrl + C in the terminal to stop running scripts.