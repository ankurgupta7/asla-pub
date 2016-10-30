from ...flask_website import FlaskWebsiteBackend
import unittest
import logging


class FlaskWebsiteBackendTestCase(unittest.TestCase):
    def setUp(self):
        FlaskWebsiteBackend.app.config['TESTING'] = True
        self.app = FlaskWebsiteBackend.app.test_client()
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_welcome(self):
        result = self.app.get("/")
        self.logger.debug(result.data)
        self.assertEqual(result.status_code, 200)

    def test_signup(self):
        result = self.app.get("/signup")
        self.logger.debug(result.data)
        self.assertEqual(result.status_code, 200)

    def test_login(self):
        result = self.app.get("/login")
        self.logger.debug(result.data)
        self.assertEqual(result.status_code, 200)

    def test_update(self):
        result = self.app.post("/update")
        self.logger.debug(result.data)
        assert 'Update' in result.data

    def test_authenticate(self):
        result = self.app.post("/authenticate")
        self.logger.debug(result.data)
        assert 'Authenticate' in result.data


if __name__ == '__main__':
    unittest.main()
