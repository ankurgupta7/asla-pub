import os, sys
root_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(root_path)
from ..leap_tools.gesture_collection import GestureCollection


class TrainingService:
    """
    Expert user invokes this service.
    - Collects data from Leap Motion
    - Sends the collected data to the server?!
    """
    def __init__(self):
        # this is the final data set that is sent to the server
        # for now, this will be stored locally in a csv file
        self.data_collected = []
        pass

    def capture_gesture(self, label):
        """
        Captures a gesture for a given label.
        Adds the gesture data to data_collected, which is then sent to the server once the process is over
        :param label: Label for current gesture being collected
        :type label: String
        """
        exp_ges = GestureCollection(label)
        exp_ges.wait_for_connection()
        if not exp_ges.is_calibrated():
            exp_ges.calibration.calibrate()
        self.data_collected.extend(exp_ges.extract_features())

    def send_to_server(self):
        """
        Sends the data to Controller(Server)
        """
        return None
