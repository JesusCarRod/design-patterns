from decimal import Decimal
from typing import ClassVar

from behavioral.strategy.client_type import ClientType
from behavioral.strategy.big_order_discount_strategy import BigOrderDiscountStrategy
from behavioral.strategy.discount_strategy import DiscountStrategy
from behavioral.strategy.no_discount_strategy import NoDiscountStrategy
from behavioral.strategy.vip_discount_strategy import VipDiscountStrategy


class DiscountStrategyResolver:
    __BIG_ORDER_THRESHOLD: ClassVar[Decimal] = Decimal("1000")

    def resolve(self, amount: Decimal, client_type: ClientType) -> DiscountStrategy:
        if amount >= self.__BIG_ORDER_THRESHOLD:
            return BigOrderDiscountStrategy()
        if client_type == ClientType.VIP:
            return VipDiscountStrategy()
        return NoDiscountStrategy()
