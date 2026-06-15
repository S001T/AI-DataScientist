import anthropic

from .base_provider import (
    BaseProvider
)


class ClaudeProvider(
    BaseProvider
):

    def __init__(
        self,
        api_key
    ):

        self.client = anthropic.Anthropic(
            api_key=api_key
        )

    def ask(
        self,
        prompt
    ):

        response = (
            self.client.messages.create(
                model="claude-sonnet-4-0",
                max_tokens=4000,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        return (
            response.content[0].text
        )