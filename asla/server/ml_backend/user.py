from profile import Profile
from binary.ml_tools.predict_service import PredictService


class User(Profile):
    """
    User Profile
    inherits Profile
    """
    def __init__(self):
        Profile.__init__(self)
        self.predict_service = PredictService()
        self.predicted_label = None

    def start_predict_service(self):
        """
        Invokes the predict service. Converts gesture to label
        :return label(This is displayed on the screen)
        """
        self.predict_service.capture_gesture()
        self.predicted_label = self.predict_service.predict_label()
        return self.predicted_label
