from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from behavioral.event_subscriber.domain.event import Event

EventT = TypeVar("EventT", bound=Event)


class Subscriber(ABC, Generic[EventT]):
    @abstractmethod
    def consume(self, event: EventT) -> None:
        pass

    @classmethod
    def fqn(cls) -> str:
        return f"{cls.__module__}.{cls.__name__}"
