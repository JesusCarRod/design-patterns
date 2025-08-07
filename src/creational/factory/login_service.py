from creational.factory.authenticator_factory import AuthenticatorFactory
from creational.factory.login_method import LoginMethod
from creational.factory.login_result import LoginResult


class LoginService:
    def login(self, login_method: LoginMethod, user_id: int, token: str) -> LoginResult:
        authenticator = AuthenticatorFactory().create(login_method)
        login_result = authenticator.authenticate(user_id=user_id, token=token)

        if login_result.success is True:
            print(f"User {user_id} successfully logged with {authenticator}")

        return login_result
