from __future__ import annotations

from typing import Any

from creational.builder.json_report import JSONReport
from creational.builder.report_builder import ReportBuilder


class JSONReportBuilder(ReportBuilder):
    def __init__(self) -> None:
        self.__reset_instance()

    def __reset_instance(self) -> None:
        self.__instance = JSONReport(title="")

    def reset(self) -> JSONReportBuilder:
        self.__reset_instance()
        return self

    def set_title(self, title: str) -> JSONReportBuilder:
        self.__instance.title = title
        return self

    def set_headers(self, headers: list[str]) -> JSONReportBuilder:
        self.__instance.headers = headers.copy()
        return self

    def set_data(self, data: list[dict[str, Any]]) -> JSONReportBuilder:
        self.__instance.data = data.copy()
        return self

    def set_metadata(self, metadata: dict[str, Any]) -> JSONReportBuilder:
        self.__instance.metadata = metadata.copy()
        return self

    def build(self) -> JSONReport:
        report = self.__instance
        self.__reset_instance()
        return report
