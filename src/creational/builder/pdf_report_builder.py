from __future__ import annotations

from typing import Any

from creational.builder.pdf_report import PDFReport
from creational.builder.report_builder import ReportBuilder


class PDFReportBuilder(ReportBuilder):
    def __init__(self) -> None:
        self.__reset_instance()

    def __reset_instance(self) -> None:
        self.__instance = PDFReport(title="")

    def reset(self) -> PDFReportBuilder:
        self.__reset_instance()
        return self

    def set_title(self, title: str) -> PDFReportBuilder:
        self.__instance.title = title
        self.__instance.metadata["title"] = title
        return self

    def set_headers(self, headers: list[str]) -> PDFReportBuilder:
        self.__instance.headers = headers.copy()
        return self

    def set_data(self, data: list[dict[str, Any]]) -> PDFReportBuilder:
        self.__instance.data = data.copy()
        return self

    def set_metadata(self, metadata: dict[str, Any]) -> PDFReportBuilder:
        self.__instance.metadata = metadata.copy()
        return self

    def build(self) -> PDFReport:
        report = self.__instance
        self.__reset_instance()
        return report
