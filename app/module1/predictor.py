import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path("C:\\Users\\yshel\\Desktop\\DivyaPath-Ai\\models\\student_model.pkl")
ENCODER_PATH = Path("C:\\Users\\yshel\\Desktop\\DivyaPath-Ai\\models\\grade_encoder.pkl")

def load_model():
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    return model, encoder

def predict_grade(model, encoder, study_hours, attendance, previous_grade, extra_val, parent_val):
    input_data = np.array([[study_hours, attendance, previous_grade, extra_val, parent_val]])
    pred = model.predict(input_data)
    return encoder.inverse_transform(pred)[0]
