import logging
import unittest

from ..binary_helper import BinaryService


class BinaryServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_fetch_binary(self):
        result = BinaryService.fetch_binary("Master")
        assert result is None
