from .llm.openai_provider import OpenAIProvider
from .llm.claude_provider import ClaudeProvider


class AIAnalyzer:

    def __init__(
        self,
        provider,
        api_key
    ):

        self.provider_name = provider

        if provider == "openai":

            self.provider = OpenAIProvider(
                api_key
            )

        elif provider == "claude":

            self.provider = ClaudeProvider(
                api_key
            )

        else:

            raise ValueError(
                "provider must be openai or claude"
            )

    def analyze(
        self,
        statistics
    ):

        prompt = f"""
You are a senior data scientist.

Analyze dataset statistics:

{statistics}

Give:
1. Key findings
2. Problems
3. Recommendations
4. Modeling ideas
"""

        return self.provider.ask(
            prompt
        )