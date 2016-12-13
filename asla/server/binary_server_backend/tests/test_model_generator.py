from ..model_generator import ModelGenerator
from ..classifier import SVM
import unittest
import logging


class GlobalModelServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG
        self.classifier = SVM()
        self.model_gen = ModelGenerator(self.classifier)

    def test_get_data(self):
        x, y = self.model_gen.get_data()
        assert (x is not None and y is not None)

if __name__ == '__main__':
    unittest.main()
