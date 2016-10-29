import unittest
from ..training_service import TrainingService


class TestTrainService(unittest.TestCase):
    def test_send_to_server(self):
        sent = TrainingService.send_to_server()
        assert sent is None

if __name__ == '__main__':
    unittest.main()
