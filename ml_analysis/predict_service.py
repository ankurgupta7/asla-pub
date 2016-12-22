from sklearn.externals import joblib
from gesture_collection import GestureCollection
import numpy as np


class PredictService:

    def __init__(self):
        self.model = joblib.load('527pm_model.pkl')
        self.scaler = joblib.load('527pm_scaler.pkl')
        self.to_predict = []
        pass

    def capture_gesture(self):
        user_ges = GestureCollection('a')
        user_ges.wait_for_connection()
        if not user_ges.is_calibrated():
            user_ges.calibration.calibrate()
        self.to_predict = user_ges.extract_features(reps=1, skip_time=0.25, hold_time=1, print_feat=False)

    def predict_label(self):
        self.to_predict = self.to_predict[0][1:].reshape(1, -1)
        to_predict_scaled = self.scaler.transform(self.to_predict)
        label = self.model.predict(to_predict_scaled)
        return chr(label + 64)
