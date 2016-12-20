from ...flask_website import FlaskWebsiteBackend
import unittest
import logging
import random, string

def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


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

    def test_authenticate(self):
        result = self.app.post("/authenticate", data=dict(email=randomword(5), pwd=randomword(5)))
        self.logger.debug(result.data)
        assert 'Invalid credentials' in result.data


if __name__ == '__main__':
    unittest.main()
