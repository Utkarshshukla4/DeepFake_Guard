# DF-Guard: Deepfake Detection System

## About the Project

DF-Guard is an AI-powered cybersecurity project developed to detect deepfake videos and audio using deep learning techniques.

The project provides a Streamlit dashboard for video analysis and also supports real-time deepfake detection using a webcam.

---

## Main Features

* Real-time deepfake detection using webcam
* Deepfake video analysis
* AI-generated and modified audio detection
* CNN-based deep learning model
* Spectral feature analysis for audio
* Streamlit-based detection dashboard
* Fake probability analysis
* Cybersecurity application for detecting media manipulation

---

## Technologies Used

* **Python** – Core development
* **Deep Learning** – Media detection
* **CNN** – Face analysis
* **Spectral Analysis** – Audio analysis
* **OpenCV** – Video processing
* **Streamlit** – Web dashboard

---

## Project Structure

```text
DF-Guard/
│
├── main.py
├── requirements.txt
├── README.md
│
├── model/
│   ├── ...
│   └── utils/
│       └── app/
│           └── dashboard.py
│
└── ...
```

---

## How It Works

```text
Video / Audio Input
        ↓
Preprocessing
        ↓
AI Model Analysis
        ↓
Feature Detection
        ↓
REAL / FAKE Prediction
        ↓
Detection Result
```

The system processes the uploaded or live media, extracts relevant features, and uses the trained models to determine whether the content is real or manipulated.

---

## Installation & Setup

### 1. Create Virtual Environment

```bash
python -m venv env
```

### 2. Activate Virtual Environment

Windows:

```bash
env\Scripts\activate
```

### 3. Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Option 1: Live Detection

Run:

```bash
python main.py
```

The application opens the webcam and displays the detection result as **REAL** or **FAKE**.

Press **Q** to exit the live detection window.

### Option 2: Streamlit Dashboard

Run:

```bash
streamlit run model/utils/app/dashboard.py
```

The Streamlit dashboard opens in a web browser.

Users can upload a video for analysis and view the predicted fake probability.

---

## Detection Output

The system provides results such as:

```text
Prediction: REAL
Fake Probability: 12%

Prediction: FAKE
Fake Probability: 87%
```

The result helps users understand the likelihood that the analyzed media has been manipulated.

---

## Security Application

DF-Guard can be used as a cybersecurity solution for identifying manipulated digital media.

It can help in detecting deepfake content used for misinformation, impersonation, identity manipulation, and other forms of digital media abuse.

---

## Limitations

* Detection accuracy depends on the trained model and input quality.
* Real-time detection requires a working webcam.
* The project is primarily designed for educational and demonstration purposes.
* Very high-quality or previously unseen deepfakes may not always be detected correctly.

---

## Future Improvements

* Improve model accuracy with larger datasets
* Support additional video formats
* Add real-time audio detection
* Improve live webcam performance
* Deploy the system as a cloud-based application
* Add advanced deepfake detection models

---

## Stop the Project

To stop the Streamlit application or running script, press:

```text
Ctrl + C
```

in the terminal.

---

## Author

**Utkarsh Shukla**

AI & Cybersecurity Project | Deep Learning | Deepfake Detection
