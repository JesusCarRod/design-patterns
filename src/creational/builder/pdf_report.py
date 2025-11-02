from enum import StrEnum
from dataclasses import dataclass

from creational.builder.report import Report
from creational.builder.report_format import ReportFormat


class PageOrientation(StrEnum):
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"


@dataclass
class PDFReport(Report):
    format: ReportFormat = ReportFormat.PDF
    orientation: PageOrientation = PageOrientation.VERTICAL

    def get_content(self) -> str:
        content = [
            f"PDF REPORT: {self.title}",
            f"Page orientation: {self.orientation}",
            f"Created at: {self.created_at}",
        ]

        if len(self.metadata) > 0:
            content.append("METADATA:\n")
            content.extend([f"{key}: {value}" for key, value in self.metadata.items()])

        if len(self.data) > 0:
            content.append("|".join(self.headers).upper())
            content.extend(["|".join(str(row.get(header)) for header in self.headers) for row in self.data])

        return "\n".join(content)
