from creational.factory.authenticator import Authenticator
from creational.factory.login_result import LoginResult


class PasswordAuthenticator(Authenticator):
    def authenticate(self, user_id: int, token: str) -> LoginResult:
        # Some validation logic with user_id and token
        return LoginResult(user_id=user_id, success=True)

    def __str__(self) -> str:
        return "Password Authenticator"
