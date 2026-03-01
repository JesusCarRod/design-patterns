from behavioral.event_subscriber.domain.order_created_event import OrderCreatedEvent
from behavioral.event_subscriber.domain.subscriber import Subscriber


class OrderCreatedSubscriber(Subscriber[OrderCreatedEvent]):
    __slots__ = ()

    def consume(self, event: OrderCreatedEvent) -> None:
        print(f"Updating inventory for created order: {event.order_id}")

        # Update the inventory based on the order items
