""" Expert user invokes this service.
- Collect data from Leap Motion
- Save collected data as csv(for now)
Todo:
- Send the collected data to the server?!

"""
from expert_gesture_collection import ExpertGestureCollection
from calibration import Calibration


class UpdateService:
    def __init__(self):
        self.label = ''
        pass

    @staticmethod
    def get_label_from_user():
        print "Enter Label(Int 1 to 5): "
        return raw_input()

    @staticmethod
    def get_single_gesture_data(label, cal_param):
        exp_ges = ExpertGestureCollection(label)
        exp_ges.wait_for_connection()
        return exp_ges.extract_features(cal_param)

    @staticmethod
    def calibrate():
        cal = Calibration()
        cal.wait_for_connection()
        return cal.calibrate()
