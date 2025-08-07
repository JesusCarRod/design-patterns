from dataclasses import dataclass


@dataclass(frozen=True)
class LoginResult:
    user_id: int
    success: bool
    error: str | None = None
