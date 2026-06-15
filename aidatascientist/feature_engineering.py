import pandas as pd
import numpy as np


class FeatureEngineer:

    def __init__(self, df):
        self.df = df.copy()

    def numeric_features(self):

        numeric = self.df.select_dtypes(
            include=np.number
        )

        for col in numeric.columns:

            self.df[f"{col}_squared"] = (
                self.df[col] ** 2
            )

            self.df[f"{col}_sqrt"] = np.sqrt(
                abs(self.df[col])
            )

        return self

    def datetime_features(self):

        for col in self.df.columns:

            try:

                converted = pd.to_datetime(
                    self.df[col]
                )

                self.df[f"{col}_year"] = (
                    converted.dt.year
                )

                self.df[f"{col}_month"] = (
                    converted.dt.month
                )

                self.df[f"{col}_day"] = (
                    converted.dt.day
                )

            except:
                pass

        return self

    def generate(self):

        return (
            self.numeric_features()
            .datetime_features()
            .df
        )