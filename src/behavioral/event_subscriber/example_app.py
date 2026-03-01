from decimal import Decimal

from behavioral.event_subscriber.application.update_inventory.order_created_subscriber import (
    OrderCreatedSubscriber as UpdateInventoryOrderCreatedSubscriber,
)
from behavioral.event_subscriber.application.update_user_loyalty.order_created_subscriber import (
    OrderCreatedSubscriber as UpdateUserLoyaltyOrderCreatedSubscriber,
)
from behavioral.event_subscriber.domain.order import OrderItem
from behavioral.event_subscriber.domain.order_created_event import OrderCreatedEvent
from behavioral.event_subscriber.domain.order_creator import OrderCreator
from behavioral.event_subscriber.infrastructure.sync_event_bus import SyncEventBus


def main() -> None:
    print("::::::::::::::::: Event Subscriber :::::::::::::::::")

    # In the app settings
    event_bus = SyncEventBus()
    event_bus.subscribe(OrderCreatedEvent, UpdateInventoryOrderCreatedSubscriber())
    event_bus.subscribe(OrderCreatedEvent, UpdateUserLoyaltyOrderCreatedSubscriber())

    # In the client creating the order
    order_creator = OrderCreator()
    order = order_creator.create(
        items=[
            OrderItem(product_id=1, quantity=1, unit_price=Decimal(100)),
            OrderItem(product_id=2, quantity=2, unit_price=Decimal(200)),
        ]
    )
    print(f"Order created with id: {order.id}")
    order_created_event = OrderCreatedEvent(order_id=order.id)
    event_bus.publish(order_created_event)


if __name__ == "__main__":
    main()
