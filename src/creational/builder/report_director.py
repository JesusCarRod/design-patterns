from creational.builder.report_builder import ReportBuilder
from creational.builder.report import Report


SAMPLE_SALES_DATA = [
    {"product": "Laptop", "quantity": 5, "total": 5000.00, "date": "2024-01-15"},
    {"product": "Mouse", "quantity": 20, "total": 400.00, "date": "2024-01-16"},
    {"product": "Keyboard", "quantity": 15, "total": 750.00, "date": "2024-01-17"},
    {"product": "Monitor", "quantity": 8, "total": 2400.00, "date": "2024-01-18"},
]

SAMPLE_USERS_DATA = [
    {"id": 1, "name": "Juan Perez", "email": "juan@example.com", "active": True},
    {"id": 2, "name": "María Garcia", "email": "maria@example.com", "active": True},
    {"id": 3, "name": "Carlos Lopez", "email": "carlos@example.com", "active": False},
]


class ReportDirector:
    def __init__(self, builder: ReportBuilder) -> None:
        self.__builder = builder
        self.__builder.reset()

    @property
    def builder(self) -> ReportBuilder:
        return self.__builder

    @builder.setter
    def builder(self, builder: ReportBuilder) -> None:
        self.__builder = builder
        self.__builder.reset()

    def build_sales_report(self) -> Report:
        report = (
            self.__builder.set_title("Sales Report")
            .set_headers(["product", "quantity", "total", "date"])
            .set_data(SAMPLE_SALES_DATA)
            .set_metadata(
                {
                    "report_type": "sales",
                    "total_amount": sum(item["total"] for item in SAMPLE_SALES_DATA),
                }
            )
            .build()
        )
        return report

    def build_users_report(self) -> Report:
        report = (
            self.__builder.set_title("Users Report")
            .set_headers(["id", "name", "email", "active"])
            .set_data(SAMPLE_USERS_DATA)
            .set_metadata(
                {
                    "report_type": "user",
                    "total_users": len(SAMPLE_USERS_DATA),
                    "active_users": sum(
                        1 for user in SAMPLE_USERS_DATA if user["active"] is True
                    ),
                }
            )
            .build()
        )
        return report
