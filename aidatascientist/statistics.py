import pandas as pd
import numpy as np


class StatisticsAnalyzer:

    def __init__(self, df):
        self.df = df

    def shape(self):
        return self.df.shape

    def columns(self):
        return list(self.df.columns)

    def dtypes(self):
        return {
            col: str(dtype)
            for col, dtype in self.df.dtypes.items()
        }

    def missing_values(self):
        return self.df.isnull().sum().to_dict()

    def duplicate_rows(self):
        return int(self.df.duplicated().sum())

    def numeric_columns(self):
        return list(
            self.df.select_dtypes(
                include=np.number
            ).columns
        )

    def categorical_columns(self):
        return list(
            self.df.select_dtypes(
                include="object"
            ).columns
        )

    def describe(self):
        result = (
        self.df
        .describe(include="all")
        .fillna("")
        .to_dict()
    )

        return result

    def correlation(self):

        numeric = self.df.select_dtypes(
            include=np.number
        )

        if len(numeric.columns) < 2:
            return {}

        return numeric.corr().to_dict()

    def full_report(self):

        return {
            "shape": self.shape(),
            "columns": self.columns(),
            "dtypes": self.dtypes(),
            "missing": self.missing_values(),
            "duplicates": self.duplicate_rows(),
            "numeric_columns": self.numeric_columns(),
            "categorical_columns": self.categorical_columns(),
            "describe": self.describe(),
            "correlation": self.correlation()
        }