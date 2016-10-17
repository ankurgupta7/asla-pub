"""
Expert user invokes this service.
- Collect data from Leap Motion
- Save collected data as csv(for now)
Todo:
- Send the collected data to the server?!
"""
from gesture_collection import GestureCollection
import numpy as np
import time


class UpdateService:
    def __init__(self):
        self.label = None
        # this is the final data set that is sent to the server
        # for now, this will be stored locally in a csv file
        self.data_collected = []
        pass

    def capture_gesture(self, label):
        exp_ges = GestureCollection(label)
        exp_ges.wait_for_connection()
        if not exp_ges.is_calibrated():
            exp_ges.calibration.calibrate()
        self.data_collected.extend(exp_ges.extract_features())

    def save_collected_data(self):
        to_save = np.array(self.data_collected)
        filename = ''.join(['data-', time.strftime("%Y%m%d-%H%M%S"), '.csv'])
        np.savetxt(filename, to_save, delimiter=',', fmt='%1.3f')
