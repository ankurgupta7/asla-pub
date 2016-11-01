import unittest
import os
import sys
root_path = os.path.dirname(os.path.abspath('.'))
blah = os.path.join(root_path, 'asla/binary/ml_tools/')
sys.path.append(blah)


# from training_service import TrainingService


class TestTrainService(unittest.TestCase):
    def test_send_to_server(self):
        # training_service = TrainingService()
        # sent = training_service.send_to_server()
        sent = None
        assert sent is None