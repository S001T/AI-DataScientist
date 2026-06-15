from openai import OpenAI

from .base_provider import (
    BaseProvider
)


class OpenAIProvider(
    BaseProvider
):

    def __init__(
        self,
        api_key
    ):

        self.client = OpenAI(
            api_key=api_key
        )

    def ask(
        self,
        prompt
    ):

        response = (
            self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )