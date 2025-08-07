from creational.factory.login_method import LoginMethod
from creational.factory.login_service import LoginService


def main() -> None:
    login_service = LoginService()

    print("::::::::::::::::: Password Login :::::::::::::::::")
    login_service.login(
        login_method=LoginMethod.PASSWORD, user_id=1, token="<PASSWORD>"
    )

    print("::::::::::::::::: Google Login :::::::::::::::::")
    login_service.login(
        login_method=LoginMethod.GOOGLE_SSO, user_id=2, token="<GOOGLE_TOKEN>"
    )

    print("::::::::::::::::: Github Login :::::::::::::::::")
    login_service.login(
        login_method=LoginMethod.GITHUB_SSO, user_id=2, token="<GITHUB_TOKEN>"
    )


if __name__ == "__main__":
    main()
