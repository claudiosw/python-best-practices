""" This module has supporting code to demonstrate testing
"""


import random
from abc import ABC, abstractmethod


def run_dice() -> str:
    """ Simulate a dice roll
    :returns: 'Lucky' or 'Unlucky'
    """
    dice = random.randint(1, 6)
    if dice < 4:
        return "Unlucky"
    return "Lucky"


class ExampleRepositoryInterface(ABC):
    """ Abstract class for ExampleRepository
    """
    @abstractmethod
    def create(self, name: str) -> str:
        """ Create Example
        :param name: Name
        :return: A String
        """


class CreateExampleUseCase():
    """ Class CreateExampleUseCase
    """
    def __init__(self, repository: ExampleRepositoryInterface) -> None:
        self.repository = repository

    def execute(self, name: str) -> str:
        """ Method to execute use case
        :param name: Name of example
        :return: Str
        """
        return self.repository.create(name)
