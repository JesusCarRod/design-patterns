from __future__ import annotations


class Singleton:
    """
    A base class to inherit from other classes and make them singleton.
    It allows class inheritance but is not thread-safe.
    """

    __instances: dict[type, Singleton] = {}
    __is_initialized: dict[type, bool] = {}

    def __new__(cls, *args, **kwargs) -> Singleton:
        if cls not in Singleton.__instances:
            Singleton.__instances[cls] = super(Singleton, cls).__new__(cls)
        return Singleton.__instances[cls]

    def __init__(self, *args, **kwargs) -> None:
        if Singleton.__is_initialized.get(self.__class__, False) is True:
            return
        Singleton.__is_initialized[self.__class__] = True
        self._setup(*args, **kwargs)

    def _setup(self, *args, **kwargs) -> None:
        pass

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        if "__init__" in cls.__dict__:
            raise TypeError(
                f"Singleton subclass {cls.__name__} cannot override __init__. Use _setup() instead."
            )
