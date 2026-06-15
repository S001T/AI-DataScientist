import pandas as pd
from .statistics import StatisticsAnalyzer
from .preprocessing import DataCleaner
from .feature_engineering import FeatureEngineer
from .automl import AutoMLTrainer
from .visualization import Visualizer
from .reports import ReportGenerator
from .ai_analysis import AIAnalyzer
from .chat_with_dataset import DatasetChat

class DataAgent:

    def __init__(self):

        self.df = None
        self.statistics = None
        self.provider = None

    def load(self, file_path):

        if file_path.endswith(".csv"):

            self.df = pd.read_csv(
                file_path
            )

        elif file_path.endswith(".xlsx"):

            self.df = pd.read_excel(
                file_path
            )

        else:

            raise ValueError(
                "Only csv and xlsx supported"
            )

        return self.df

    def clean(self):

        cleaner = DataCleaner(
            self.df
        )

        self.df = (
            cleaner
            .remove_duplicates()
            .fill_missing()
            .remove_constant_columns()
            .get_dataframe()
        )

        return self.df

    def analyze(self):

        analyzer = StatisticsAnalyzer(
            self.df
        )

        self.statistics = (
            analyzer.full_report()
        )

        return self.statistics

    def engineer_features(self):

        engineer = FeatureEngineer(
            self.df
        )

        self.df = engineer.generate()

        return self.df

    def visualize(self):

        visualizer = Visualizer(
            self.df
        )

        return visualizer.create_all()

    def train_model(
        self,
        target
    ):

        trainer = AutoMLTrainer(
            self.df,
            target
        )

        return trainer.train()

    def connect_llm(
        self,
        provider
    ):

        self.provider = provider

    def ask(
        self,
        question
    ):

        if self.provider is None:

            raise ValueError(
                "LLM provider not connected"
            )

        chat = DatasetChat(
            self.df,
            self.provider
        )

        return chat.ask(
            question
        )

    def ai_analyze(
        self,
        provider_name,
        api_key
    ):

        ai = AIAnalyzer(
            provider_name,
            api_key
        )

        return ai.analyze(
            self.statistics
        )

    def save_report(
        self,
        html=True
    ):

        report = ReportGenerator(
            self.statistics
        )

        if html:

            return report.save_html()

        return report.save_json()

    def head(
        self,
        n=5
    ):

        return self.df.head(n)

    def columns(self):

        return list(
            self.df.columns
        )

    def shape(self):

        return self.df.shape
    
    def version(self):
        
        return "1.0.0"