
import pandas as pd
import numpy as np


class DataCleaner:

    def __init__(self, df):
        self.df = df.copy()

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()
        return self

    def fill_missing(self):

        for col in self.df.columns:

            if self.df[col].dtype == "object":

                mode = self.df[col].mode()

                if len(mode):
                    self.df[col] = self.df[col].fillna(mode[0])
                else:
                    self.df[col] = self.df[col].fillna("Unknown")

            else:

                self.df[col] = self.df[col].fillna(
                    self.df[col].median()
                )

        return self

    def remove_constant_columns(self):

        cols_to_drop = []

        for col in self.df.columns:

            if self.df[col].nunique() <= 1:
                cols_to_drop.append(col)

        self.df = self.df.drop(
            columns=cols_to_drop,
            errors="ignore"
        )

        return self

    def get_dataframe(self):
        return self.df