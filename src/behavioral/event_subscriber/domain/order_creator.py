from datetime import datetime
from uuid import uuid4

from behavioral.event_subscriber.domain.order import Order, OrderItem


class OrderCreator:
    def create(self, items: list[OrderItem]) -> Order:
        return Order(id=str(uuid4()), items=items, created_at=datetime.now(), updated_at=datetime.now())
