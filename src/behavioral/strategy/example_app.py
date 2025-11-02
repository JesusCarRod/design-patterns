from dataclasses import asdict
from decimal import Decimal

from behavioral.strategy.client_type import ClientType
from behavioral.strategy.discount_strategy_resolver import DiscountStrategyResolver
from behavioral.strategy.order_processor import OrderProcessor


def main() -> None:
    print("\n::::::::::::::::: Order processing :::::::::::::::::\n")

    order_processor = OrderProcessor(discount_strategy_resolver=DiscountStrategyResolver())

    orders: list[tuple[Decimal, ClientType]] = [
        (Decimal("100"), ClientType.REGULAR),
        (Decimal("300"), ClientType.VIP),
        (Decimal("3000"), ClientType.REGULAR),
        (Decimal("1500"), ClientType.VIP),
    ]
    for amount, client_type in orders:
        print(f"\nProcessing order with amount: {amount} and client type: {client_type}")

        result = order_processor.process(amount=amount, client_type=client_type)

        print(f"Order result: {asdict(result)}")


if __name__ == "__main__":
    main()
