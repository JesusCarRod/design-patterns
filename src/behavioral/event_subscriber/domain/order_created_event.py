from dataclasses import dataclass

from behavioral.event_subscriber.domain.event import Event


@dataclass(frozen=True)
class OrderCreatedEvent(Event):
    order_id: str
