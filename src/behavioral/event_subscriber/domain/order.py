from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime


@dataclass(frozen=True)
class OrderItem:
    product_id: int
    quantity: int
    unit_price: Decimal


@dataclass(frozen=True)
class Order:
    id: str
    items: list[OrderItem]
    created_at: datetime
    updated_at: datetime

    @property
    def total_amount(self) -> Decimal:
        return sum((item.unit_price * item.quantity for item in self.items), Decimal(0))
