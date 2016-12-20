from .. import ASLAController
import unittest
import logging


class ASLAControllerTestCase(unittest.TestCase):
    def setUp(self):
        ASLAController.app.config['TESTING'] = True

        self.app = ASLAController.app.test_client()
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_get_model(self):
        result = self.app.post("/getmodel", data=dict(
            time='20161213-010905',
        ))
        self.logger.debug(result.data)
        assert result.data is not None

    # def test_make_model(self):
    #     result = self.app.post("/train", data=dict(
    #         store='False'
    #     ))
    #     self.logger.debug(result.data)
    #     assert 'makemodel' in result.data

if __name__ == '__main__':
    unittest.main()
