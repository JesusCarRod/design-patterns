from enum import StrEnum


class LoginMethod(StrEnum):
    PASSWORD = "password"
    GOOGLE_SSO = "google_sso"
    GITHUB_SSO = "github_sso"
