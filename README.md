## Contact

**Utkarsh Shukla**

Email- utqrshkumar07@gmail.com

Github- https://github.com/Utkarshshukla4

##  Overview

Deepfake Guard identifies synthetic or manipulated media using pretrained deep learning models.  
It can detect deepfake faces, voice manipulations, and altered content patterns.


##  Features

- Real-Time Detects video & audio deepfakes  
- Confidence scoring per file  
- Visual explanation of manipulated frames  
- CLI-based and lightweight  
- Streamlit Dashboard


##  Architecture

[Video / Audio Input]
      ↓
[Frame / Audio Feature Extraction]
      ↓
[Deepfake Detection Model (CNN/LSTM)]
      ↓
[Output: Real / Fake + Confidence Score]


## Project Structure

deepfake-guard/
├── src/
├── models/
├── docs/
│   └── architecture.png
├── requirements.txt
├── README.md
└── .gitignore


##  Installation

git clone https://github.com/Utkarshshukla4/DeepFake_Guard.git

cd DeepFake_Guard

pip install -r requirements.txt {Windows}

python3 -m pip install -r requirements.txt {Linux}


## Activate the Environment

_Windows:_

python -m venv env

env\Scripts\activate

_Linux / Mac:_

python3 -m venv env

source env/bin/activate


## Run the Project

_Option 1:_ **Live Detection (Webcam)** 

python main.py


  -Opens a live webcam window with “REAL” or “FAKE” overlay.

  -Press Q to exit.


_Option 2:_ **Streamlit Dashboard**

streamlit run model/utils/app/dashboard.py


  -Opens a browser dashboard to upload a video for detection.

  -Shows the fake probability percentage.

## Input Example

Upload a short video or audio clip.

 ## Output Example
 
Result: Deepfake Detected  

Confidence: 91%

## Stop the Project

Press Ctrl + C in the terminal to stop running scripts.

## Summary

Deepfake Guard uses CNN-LSTM architecture to differentiate real and AI-generated multimedia.







