from functools import wraps
from typing import Callable


class Registry:
    __registry: dict[str, type] = {}

    @classmethod
    def register(self, key: str) -> Callable[[type], type]:
        def decorator(klass: type) -> type:
            self.__registry[key] = klass
            return klass

        return decorator

    @classmethod
    def get(self, key: str):
        klass = self.__registry.get(key)
        if klass is None:
            raise ValueError(f"No class registered with key: {key}")
        return klass()
