import FlaskWebsiteBackend
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
        assert 'Welcome to Asla' in result.data

    def test_signup(self):
        result = self.app.post("/signup")
        self.logger.debug(result.data)
        assert 'Signup' in result.data

    def test_login(self):
        result = self.app.post("/login")
        self.logger.debug(result.data)
        assert 'Login' in result.data

    def test_update(self):
        result = self.app.post("/login")
        self.logger.debug(result.data)
        assert 'Login' in result.data

    def test_login(self):
        result = self.app.post("/login")
        self.logger.debug(result.data)
        assert 'Login' in result.data


if __name__ == '__main__':
    unittest.main()
