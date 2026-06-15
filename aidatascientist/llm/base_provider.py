from abc import ABC
from abc import abstractmethod


class BaseProvider(
    ABC
):

    @abstractmethod
    def ask(
        self,
        prompt
    ):
        pass