from decimal import Decimal

from behavioral.strategy.discount_strategy import DiscountStrategy


class NoDiscountStrategy(DiscountStrategy):
    def calculate_discount(self, amount: Decimal) -> Decimal:
        return Decimal("0")

    def __str__(self) -> str:
        return "No discount"
