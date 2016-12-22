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
import csv


class TrainingService:
    def __init__(self):
        self.label = None
        # this is the final collected data set
        self.data_collected = []
        pass

    def capture_gesture(self, label):
        exp_ges = GestureCollection(label)
        exp_ges.wait_for_connection()
        if not exp_ges.is_calibrated():
            exp_ges.calibration.calibrate()
        self.data_collected.extend(exp_ges.extract_features())

    def save_collected_data(self):
        with open('headers.csv', 'rb') as headers_file:
            reader = csv.reader(headers_file)
            headers = next(reader)
        filename = ''.join(['data-sri-', time.strftime("%Y%m%d-%H%M%S"), '.csv'])
        with open(filename, "wb") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerows(self.data_collected)