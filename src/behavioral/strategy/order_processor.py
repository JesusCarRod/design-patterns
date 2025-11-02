from decimal import Decimal
from dataclasses import dataclass

from behavioral.strategy.client_type import ClientType
from behavioral.strategy.discount_strategy_resolver import DiscountStrategyResolver


@dataclass(frozen=True)
class OrderResult:
    subtotal_amount: Decimal
    final_amount: Decimal
    discount_amount: Decimal
    discount_reason: str


class OrderProcessor:
    def __init__(self, discount_strategy_resolver: DiscountStrategyResolver) -> None:
        self.__discount_strategy_resolver = discount_strategy_resolver

    def process(self, amount: Decimal, client_type: ClientType) -> OrderResult:
        strategy = self.__discount_strategy_resolver.resolve(amount=amount, client_type=client_type)
        discount = strategy.calculate_discount(amount=amount)

        final_amount = amount - discount

        return OrderResult(
            subtotal_amount=amount,
            final_amount=final_amount,
            discount_amount=discount,
            discount_reason=str(strategy),
        )
