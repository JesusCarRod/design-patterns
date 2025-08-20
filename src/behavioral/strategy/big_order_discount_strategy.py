from decimal import Decimal

from behavioral.strategy.discount_strategy import DiscountStrategy


class BigOrderDiscountStrategy(DiscountStrategy):
    def calculate_discount(self, amount: Decimal) -> Decimal:
        return amount * Decimal("0.25")

    def __str__(self) -> str:
        return "Big order discount"
