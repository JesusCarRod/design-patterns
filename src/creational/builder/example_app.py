from creational.builder.json_report_builder import JSONReportBuilder
from creational.builder.pdf_report_builder import PDFReportBuilder
from creational.builder.report_director import ReportDirector


def main() -> None:
    pdf_builder = PDFReportBuilder()
    json_builder = JSONReportBuilder()
    director = ReportDirector(builder=pdf_builder)

    print("\n::::::::::::::::: Sales report in PDF :::::::::::::::::")
    sales_report_pdf = director.build_sales_report()
    print(sales_report_pdf.get_content())

    print("\n::::::::::::::::: Sales report in JSON :::::::::::::::::")
    director.builder = json_builder
    sales_report_json = director.build_sales_report()
    print(sales_report_json.get_content())

    print("\n::::::::::::::::: Users report in PDF :::::::::::::::::")
    director.builder = pdf_builder
    users_report_pdf = director.build_users_report()
    print(users_report_pdf.get_content())

    print("\n::::::::::::::::: Users report in JSON :::::::::::::::::")
    director.builder = json_builder
    users_report_json = director.build_users_report()
    print(users_report_json.get_content())


if __name__ == "__main__":
    main()
