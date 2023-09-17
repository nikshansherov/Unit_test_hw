from user import User


class UserRepository:
    def __init__(self):
        self._authenticated_users = []

    @property
    def authenticated_users(self):
        return self._authenticated_users

    def add_user(self, user, login, password):
        if not user.authenticate(login, password):
            return False
        self._authenticated_users.append(user)
        return True
