from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from creational.builder.report import Report


class ReportBuilder(ABC):
    @abstractmethod
    def reset(self) -> ReportBuilder:
        pass

    @abstractmethod
    def set_title(self, title: str) -> ReportBuilder:
        pass

    @abstractmethod
    def set_headers(self, headers: list[str]) -> ReportBuilder:
        pass

    @abstractmethod
    def set_data(self, data: list[dict[str, Any]]) -> ReportBuilder:
        pass

    @abstractmethod
    def set_metadata(self, metadata: dict[str, Any]) -> ReportBuilder:
        pass

    @abstractmethod
    def build(self) -> Report:
        pass
