from behavioral.event_subscriber.domain.order_created_event import OrderCreatedEvent
from behavioral.event_subscriber.domain.subscriber import Subscriber


class OrderCreatedSubscriber(Subscriber[OrderCreatedEvent]):
    def consume(self, event: OrderCreatedEvent) -> None:
        print(f"Updating user loyalty for created order: {event.order_id}")

        # Update the user loyalty based on the order items
