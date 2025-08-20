from abc import ABC, abstractmethod
from decimal import Decimal


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, amount: Decimal) -> Decimal:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
