import logging
import unittest

from ..user_admin_service import UserAdminService


class UserAdminServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger()
        self.logger.level = logging.DEBUG

    def test_make_new_user(self):
        result = UserAdminService.make_new_user()
        assert result is None

    def test_update_user(self):
        result = UserAdminService.update_user()
        assert result is None

    def test_authenticate_user(self):
        result = UserAdminService.authenticate_user()
        assert result is None
