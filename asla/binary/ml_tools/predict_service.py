from sklearn.externals import joblib
import os, sys
root_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(root_path)
from ..leap_tools.gesture_collection import GestureCollection


class PredictService:
    """
    Service for predicting gestures for users
    """

    def __init__(self, model_file, scaler_file):
        # type: (string, string)
        # do some path append to model_file and scalar_file
        print model_file
        self.model = joblib.load(model_file)
        self.scaler = joblib.load(scaler_file)
        self.to_predict = []
        self.user_ges = GestureCollection()
        pass


    def capture_gesture(self):
        """
        Captures user's gesture
        """

        self.user_ges.wait_for_connection()
        if not self.user_ges.is_calibrated():
            self.user_ges.calibration.calibrate()
        self.to_predict = self.user_ges.extract_features(reps=1, skip_time=0.25, hold_time=1, print_feat=False)

    def predict_label(self):
        """
        Predicts label for a captured gesture
        """
        self.to_predict = self.to_predict[0][1:].reshape(1, -1)
        to_predict_scaled = self.scaler.transform(self.to_predict)
        return str(self.model.predict(to_predict_scaled)[0])
    def setStatusbar(self, s):
        self.user_ges.setStatusBar(s)