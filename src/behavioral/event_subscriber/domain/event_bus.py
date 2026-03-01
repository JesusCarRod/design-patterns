from abc import ABC, abstractmethod

from behavioral.event_subscriber.domain.event import Event
from behavioral.event_subscriber.domain.subscriber import Subscriber


class EventBus(ABC):
    @abstractmethod
    def publish(self, event: Event) -> None:
        pass

    @abstractmethod
    def subscribe(self, event_class: type[Event], subscriber: Subscriber) -> None:
        pass
