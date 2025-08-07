from abc import ABC, abstractmethod

from creational.factory.login_result import LoginResult


class Authenticator(ABC):
    @abstractmethod
    def authenticate(self, user_id: int, token: str) -> LoginResult:
        pass
