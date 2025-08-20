import json
from dataclasses import dataclass

from creational.builder.report import Report
from creational.builder.report_format import ReportFormat


@dataclass
class JSONReport(Report):
    format: ReportFormat = ReportFormat.JSON
    indentation_level: int = 4

    def get_content(self) -> str:
        content = {
            "title": self.title,
            "headers": self.headers,
            "data": self.data,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }
        return json.dumps(content, indent=self.indentation_level)
