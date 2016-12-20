from sklearn.externals import joblib
import os, sys
root_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(root_path)

try:
    if os.environ["NOQT"] == "1":
        print 'gesture collection which needs qt, not being imported'
    else:
        from ..leap_tools.gesture_collection import GestureCollection
except KeyError:
    from ..leap_tools.gesture_collection import GestureCollection


class PredictService:
    """
    Service for predicting gestures for users
    """

    def __init__(self, model_file, scaler_file):
        # type: (string, string)
        # do some path append to model_file and scalar_file
        self.model = joblib.load(model_file)
        self.scaler = joblib.load(scaler_file)
        self.to_predict = []
        self.user_ges = None
        pass

    def make_gesture_obj(self):
        # trivial but needs a separate method for template design pattern
        self.user_ges = GestureCollection('@')

    def capture_gesture(self):
        """
        Captures user's gesture
        """
        if not self.user_ges.wait_for_connection():
            return False

        if not self.user_ges.is_calibrated():
            self.user_ges.calibration.calibrate()
        self.to_predict = self.user_ges.extract_features(reps=1, skip_time=0.25, hold_time=0.5 , print_feat=False)
        return True

    def predict_label(self):
        """
        Predicts label for a captured gesture
        """

        self.to_predict = self.to_predict[0][1:].reshape(1, -1)
        to_predict_scaled = self.scaler.transform(self.to_predict)
        return chr(64 + int(self.model.predict(to_predict_scaled)[0]))

    def setStatusbar(self, s):
        self.user_ges.setStatusBar(s)