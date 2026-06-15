import sqlite3
import pandas as pd


class SQLAgent:

    def __init__(
        self,
        db_path,
        llm=None
    ):

        self.db_path = db_path

        self.llm = llm

        self.connection = sqlite3.connect(
            db_path
        )

    def tables(self):

        query = """
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        """

        result = pd.read_sql_query(
            query,
            self.connection
        )

        return result["name"].tolist()

    def query(
        self,
        sql
    ):

        return pd.read_sql_query(
            sql,
            self.connection
        )

    def ask(
        self,
        question
    ):

        if self.llm is None:

            raise ValueError(
                "LLM provider not connected"
            )

        tables = self.tables()

        prompt = f"""
Database tables:

{tables}

Convert the following request into SQL:

{question}

Return ONLY SQL.
"""

        sql = self.llm.ask(
            prompt
        )

        sql = sql.replace(
            "```sql",
            ""
        ).replace(
            "```",
            ""
        ).strip()

        return self.query(
            sql
        )

    def close(self):

        self.connection.close()