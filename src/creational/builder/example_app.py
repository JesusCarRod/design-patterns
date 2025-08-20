from creational.builder.json_report_builder import JSONReportBuilder
from creational.builder.pdf_report_builder import PDFReportBuilder
from creational.builder.report_director import ReportDirector


def main() -> None:
    director = ReportDirector(builder=PDFReportBuilder())

    print("\n::::::::::::::::: Sales report in PDF :::::::::::::::::")
    sales_report_pdf = director.build_sales_report()
    print(sales_report_pdf.get_content())

    print("\n::::::::::::::::: Sales report in JSON :::::::::::::::::")
    director.builder = JSONReportBuilder()
    sales_report_json = director.build_sales_report()
    print(sales_report_json.get_content())

    print("\n::::::::::::::::: Users report in PDF :::::::::::::::::")
    director.builder = PDFReportBuilder()
    users_report_pdf = director.build_users_report()
    print(users_report_pdf.get_content())

    print("\n::::::::::::::::: Users report in JSON :::::::::::::::::")
    director.builder = JSONReportBuilder()
    users_report_json = director.build_users_report()
    print(users_report_json.get_content())


if __name__ == "__main__":
    main()
