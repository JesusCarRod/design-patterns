from decimal import Decimal

from behavioral.strategy.discount_strategy import DiscountStrategy


class VipDiscountStrategy(DiscountStrategy):
    def calculate_discount(self, amount: Decimal) -> Decimal:
        return amount * Decimal("0.10")

    def __str__(self) -> str:
        return "VIP discount"
