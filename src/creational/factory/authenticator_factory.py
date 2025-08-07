from creational.factory.authenticator import Authenticator
from creational.factory.github_sso_authenticator import GithubSsoAuthenticator
from creational.factory.google_sso_authenticator import GoogleSsoAuthenticator
from creational.factory.login_method import LoginMethod
from creational.factory.password_authenticator import PasswordAuthenticator


class AuthenticatorFactory:
    def create(self, login_method: LoginMethod) -> Authenticator:
        match login_method:
            case LoginMethod.PASSWORD:
                return PasswordAuthenticator()
            case LoginMethod.GOOGLE_SSO:
                return GoogleSsoAuthenticator()
            case LoginMethod.GITHUB_SSO:
                return GithubSsoAuthenticator()
