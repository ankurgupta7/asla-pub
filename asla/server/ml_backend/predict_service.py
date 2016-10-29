from sklearn.externals import joblib
from gesture_collection import GestureCollection


class PredictService:
    """
    Service for predicting gestures for users
    """

    def __init__(self):
        self.model = joblib.load('model.pkl')
        self.scaler = joblib.load('scaler.pkl')
        self.to_predict = []
        pass

    def capture_gesture(self):
        """
        Captures user's gesture
        """
        user_ges = GestureCollection()
        user_ges.wait_for_connection()
        if not user_ges.is_calibrated():
            user_ges.calibration.calibrate()
        self.to_predict = user_ges.extract_features(reps=1, skip_time=0.25, hold_time=1, print_feat=False)

    def predict_label(self):
        """
        Predicts label for a captured gesture
        """
        self.to_predict = self.to_predict[0][1:].reshape(1, -1)
        to_predict_scaled = self.scaler.transform(self.to_predict)
        return self.model.predict(to_predict_scaled)
