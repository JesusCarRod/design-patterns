from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from creational.builder.report_format import ReportFormat


@dataclass
class Report(ABC):
    title: str
    format: ReportFormat
    headers: list[str] = field(default_factory=list)
    data: list[dict[str, Any]] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)

    @abstractmethod
    def get_content(self) -> str:
        pass

    def __post_init__(self) -> None:
        if len(self.data) > 0 and len(self.headers) != len(self.data[0]):
            raise ValueError(f"Number of headers does not match number of columns")
