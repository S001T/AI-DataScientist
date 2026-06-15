import json
from datetime import datetime


class ReportGenerator:

    def __init__(self, analysis_result):
        self.analysis_result = analysis_result

    def save_json(
        self,
        file_name="report.json"
    ):

        with open(
            file_name,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.analysis_result,
                f,
                indent=4,
                ensure_ascii=False
            )

        return file_name

    def save_html(
        self,
        file_name="report.html"
    ):

        html = f"""
        <html>
        <head>
            <title>AI Data Report</title>
        </head>

        <body>

        <h1>AI Data Scientist Report</h1>

        <h3>Date</h3>
        <p>{datetime.now()}</p>

        <pre>
{json.dumps(self.analysis_result, indent=4)}
        </pre>

        </body>
        </html>
        """

        with open(
            file_name,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(html)

        return file_name