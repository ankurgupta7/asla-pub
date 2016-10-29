from global_model_service import GlobalModelService
import unittest
import logging


class GlobalModelServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_generate_modell(self):
        result = GlobalModelService.generate_model("data")
        assert result is None

    def test_fetch_model(self):
        result = GlobalModelService.fetch_model()
        assert result is None

if __name__ == '__main__':
    unittest.main()
