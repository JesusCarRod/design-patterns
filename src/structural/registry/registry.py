from typing import Callable, TypeVar, Any

T = TypeVar("T")


class Registry:
    __registry: dict[str, type[Any]] = {}

    @classmethod
    def register(cls, key: str) -> Callable[[type[T]], type[T]]:
        def decorator(klass: type[T]) -> type[T]:
            cls.__registry[key] = klass
            return klass
        return decorator

    @classmethod
    def get(cls, key: str) -> Any:
        klass = cls.__registry.get(key)
        if klass is None:
            raise ValueError(f"No class registered with key: {key}")
        return klass()
