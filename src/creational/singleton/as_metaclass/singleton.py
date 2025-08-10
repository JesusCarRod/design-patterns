from typing import TypeVar


T = TypeVar("T")


class SingletonMeta(type):
    """
    Metaclass that makes a class using it a singleton.
    It supports inheritance but is not thread-safe.
    """

    __instances: dict[type[T], T] = {}

    def __call__(cls: type[T], *args, **kwargs) -> T:
        if cls not in cls.__instances:  # type: ignore[attr-defined]
            cls.__instances[cls] = super().__call__(*args, **kwargs)  # type: ignore[attr-defined]
        return cls.__instances[cls]  # type: ignore[attr-defined]
