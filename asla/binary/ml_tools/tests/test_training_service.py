import unittest
from ...ml_tools.training_service import TrainingService


class TestTrainService(unittest.TestCase):
    def test_send_to_server(self):
        training_service = TrainingService()
        sent = training_service.send_to_server()
        assert sent is None
