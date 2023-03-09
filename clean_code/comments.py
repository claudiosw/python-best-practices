# pylint: disable=C0116

""" This module contains examples of clean code regarding comments
"""


# Bad example
def calculate_sale_price_bad(cost_price):
    return cost_price * (1 + 50 / 100)  # 50 is margin %


# Good example
# Notice that when we name the constant, it is self-explanatory. We don't need
# to add a comment.
DEFAULT_MARGIN_PERCENT = 50


def calculate_sale_price_good(cost_price):
    return cost_price * (1 + DEFAULT_MARGIN_PERCENT / 100)


# Bad example
# Don't comment out old code
# def calculate_sale_price_bad_old_version(cost_price):
#    return cost_price * (1 + 50 / 100) # 50 is margin %


# Explain why the code was written this way
# I decided to use this way because ...


# Example of comment that we want to do in the future
# This is to disable Pylint TODO error => pylint: disable=fixme
# TODO: Add more examples here # pylint: disable=fixme
