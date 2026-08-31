import cv2
import numpy as np
from pathlib import Path
import tensorflow as tf
from keras.models import load_model
from keras import mixed_precision


# ================================
# FORCE FLOAT32 (VERY IMPORTANT)
# ================================
mixed_precision.set_global_policy("float32")

# ================================
# PROJECT ROOT
# ================================
ROOT_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "emotion_model.h5"


# ================================
# LOAD MODEL (SAFE)
# ================================
model = load_model(MODEL_PATH, compile=False)

# ================================
# EMOTION LABELS
# ================================
EMOTIONS = ["Angry", "Disgust", "Fear", "Happy", "Neutral", "Sad", "Surprise"]


# ================================
# FACE DETECTOR
# ================================
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ================================
# MAIN FUNCTION
# ================================
def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None

    (x, y, w, h) = faces[0]
    face = gray[y:y+h, x:x+w]

    face = cv2.resize(face, (48, 48))
    face = face / 255.0
    face = face.reshape(1, 48, 48, 1)

    preds = model.predict(face, verbose=0)
    return EMOTIONS[np.argmax(preds)]
