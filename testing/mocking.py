""" This module has supporting code to demonstrate testing
"""


import random


def run_dice() -> str:
    """ Simulate a dice roll
    :returns: 'Lucky' or 'Unlucky'
    """
    dice = random.randint(1, 6)
    if dice < 4:
        return "Unlucky"
    return "Lucky"
