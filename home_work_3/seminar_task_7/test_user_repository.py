import unittest
from user import User
from user_repository import UserRepository


class TestUserRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.authenticated_users = UserRepository()
        self.user = User('user_login', 'user_password')

    def test_add_user_not_authentication(self):
        self.assertFalse(self.authenticated_users.add_user(self.user, '', ''))

    def test_add_user_authentication(self):
        self.assertTrue(self.authenticated_users.add_user(self.user, 'user_login', 'user_password'))

    def test_presence_user_in_list(self):
        self.authenticated_users.add_user(self.user, 'user_login', 'user_password')
        self.assertTrue(self.user in self.authenticated_users._authenticated_users)

    def test_absence_user_in_list(self):
        self.authenticated_users.add_user(self.user, '', 'user_password')
        self.assertFalse(self.user in self.authenticated_users._authenticated_users)
