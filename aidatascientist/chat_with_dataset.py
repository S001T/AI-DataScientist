import json


class DatasetChat:

    def __init__(
        self,
        dataframe,
        llm_provider
    ):

        self.df = dataframe
        self.llm = llm_provider

    def ask(
        self,
        question
    ):

        context = {
            "shape": self.df.shape,
            "columns": list(self.df.columns),
            "sample": self.df.head(10).to_dict(),
            "correlation": self.df.corr(
                numeric_only=True
            ).to_dict(),
            "describe": self.df.describe(
                include="all"
            ).fillna("").to_dict()
        }
        prompt = f"""
You are a professional data scientist.

Dataset:

{json.dumps(context)}

Question:

{question}

Answer in detail.
"""

        return self.llm.ask(
            prompt
        )