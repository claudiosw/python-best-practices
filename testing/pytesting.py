""" Example code to show Pytest features """


import uuid
import dataclasses
import sys
from typing import Dict


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


def get_user_inputs() -> Dict[str, str]:
    """ Get User Inputs
    :return: Dictionary with user inputs
    """
    received_user_input1 = str(input("What is your first input?"))
    received_user_input2 = str(input("What is your second input?"))
    return {
        "user_input1": received_user_input1,
        "user_input2": received_user_input2
    }


def print_hello_world_with_error():
    """ Print Hello World with error """
    print("Hello World")
    sys.stderr.write("This is an error")
