import logging
import unittest
import random, string

from ..user_admin_service import UserAdminService


def randomword(length):
    return ''.join(random.choice(string.lowercase) for i in range(length))


class UserAdminServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG
        self.service = UserAdminService()

    def test_make_new_user(self):
        form = {'email': randomword(5) + "@test.com", 'name': "batman", 'pwd': "alfred"}
        result = self.service.make_new_user(form)
        assert result is True

    def test_update_user(self):
        result = self.service.update_user()
        assert result is None

    def test_authenticate_user(self):
        result = self.service.authenticate_user(randomword(5), randomword(5))
        assert result is False
