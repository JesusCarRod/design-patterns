from behavioral.event_subscriber.domain.event import Event
from behavioral.event_subscriber.domain.event_bus import EventBus
from behavioral.event_subscriber.domain.subscriber import Subscriber


class SyncEventBus(EventBus):
    __slots__ = ("__subscribers_by_event_fqn",)

    def __init__(self) -> None:
        self.__subscribers_by_event_fqn: dict[str, list[Subscriber]] = {}

    def publish(self, event: Event) -> None:
        print(f"Publishing event: {event.fqn()}")

        subscribers = self.__subscribers_by_event_fqn.get(event.fqn(), [])
        for subscriber in subscribers:
            subscriber.consume(event)

    def subscribe(self, event_class: type[Event], subscriber: Subscriber) -> None:
        self.__subscribers_by_event_fqn.setdefault(event_class.fqn(), []).append(subscriber)
