""" Example code to show Pytest features """


import uuid
import dataclasses


@dataclasses.dataclass
class Product:
    """ Class Product example """
    id: uuid.UUID
    price: float
    name: str


def add(number_1: int, number_2: int) -> int:
    """
    Add two numbers.

    :param number_1: First number.
    :param number_2: Second number.
    :return: Sum of two numbers.
    """
    return number_1 + number_2
