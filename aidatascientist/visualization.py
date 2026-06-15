from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


class Visualizer:

    def __init__(
        self,
        df,
        output_dir="charts"
    ):

        self.df = df
        self.output_dir = output_dir

        Path(
            self.output_dir
        ).mkdir(
            exist_ok=True
        )

    def histograms(self):

        created = []

        numeric = self.df.select_dtypes(
            include="number"
        )

        for col in numeric.columns:

            plt.figure(
                figsize=(8, 4)
            )

            sns.histplot(
                self.df[col]
            )

            file = (
                f"{self.output_dir}/"
                f"{col}_hist.png"
            )

            plt.savefig(file)
            plt.close()

            created.append(file)

        return created

    def correlation_heatmap(self):

        numeric = self.df.select_dtypes(
            include="number"
        )

        if len(numeric.columns) < 2:
            return None

        plt.figure(
            figsize=(10, 8)
        )

        sns.heatmap(
            numeric.corr(),
            annot=True
        )

        file = (
            f"{self.output_dir}/"
            f"correlation.png"
        )

        plt.savefig(file)
        plt.close()

        return file

    def create_all(self):

        files = []

        files.extend(
            self.histograms()
        )

        heatmap = (
            self.correlation_heatmap()
        )

        if heatmap:
            files.append(
                heatmap
            )

        return files