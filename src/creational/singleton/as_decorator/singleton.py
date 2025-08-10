from functools import wraps
from typing import TypeVar, Callable

T = TypeVar("T")


def singleton(klass: type[T]) -> Callable[..., T]:
    """
    A decorator for classes that makes them a singleton.
    It does not support inheritance and is not thread-safe.
    """

    __instance: T | None = None

    @wraps(klass)
    def get_instance(*args, **kwargs) -> T:
        nonlocal __instance
        if __instance is None:
            __instance = klass(*args, **kwargs)
        return __instance

    return get_instance
