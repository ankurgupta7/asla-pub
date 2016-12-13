import os, sys
root_path = os.path.dirname(os.path.abspath('..'))
sys.path.append(root_path)
from ..leap_tools.gesture_collection import GestureCollection
from pymongo import MongoClient

class TrainingService:
    """
    Expert user invokes this service.
    - Collects data from Leap Motion
    - Sends the collected data to the server?!
    """
    def __init__(self):
        # this is the final data set that is sent to the server
        # for now, this will be stored locally in a csv file
        self.mongo_client = MongoClient("mongodb://asla-expert:asla@ds149207.mlab.com:49207/trainingdata")
        self.db = self.mongo_client['trainingdata']
        self.model_data = self.db['globalmodeldata']
        self.data_collected = []
        self.exp_ges = GestureCollection('')
        pass

    def capture_gesture(self, label):
        """
        Captures a gesture for a given label.
        Adds the gesture data to data_collected, which is then sent to the server once the process is over
        :param label: Label for current gesture being collected
        :type label: String
        """
        self.exp_ges.label = label
        self.exp_ges.wait_for_connection()
        if not self.exp_ges.is_calibrated():
            self.exp_ges.calibration.calibrate()
        self.data_collected.extend(self.exp_ges.extract_features())

    def send_to_server(self):
        """
        Sends the captured gestures to the database server
        """
        header_string = open('headers.csv')
        headers = header_string.read().split(',')
        for row in self.data_collected:
            data_to_send = {}
            for i, header in enumerate(headers):
                data_to_send[header] = row[i]
            self.model_data.insert_one(data_to_send)

    def set_status_bar(self, s):
        self.exp_ges.setStatusBar(s)
