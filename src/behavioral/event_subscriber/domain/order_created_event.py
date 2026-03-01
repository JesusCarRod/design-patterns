from behavioral.event_subscriber.domain.event import Event
from dataclasses import dataclass


@dataclass(frozen=True)
class OrderCreatedEvent(Event):
    order_id: str
