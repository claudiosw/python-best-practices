""" This module shows examples of how to break likes when our code passes the
    79 character limit.
"""


def first_function_with_very_long_name(
        first_argument: str,
        second_argument: int) -> str:
    """ This function would pass the 79 character limit.
    """
    return f"{first_argument} {second_argument}"


def second_function_with_very_long_name(
        first_argument: str,
        second_argument: int
        ) -> str:
    """ This function would pass the 79 character limit.
    """
    return f"{first_argument} {second_argument}"


def third_function_with_very_long_name(
        first_argument: str, second_argument: int) -> str:
    """ This function would pass the 79 character limit.
    """
    return f"{first_argument} {second_argument}"


def fourth_function_with_very_long_name(
                                        first_argument: str,
                                        second_argument: int) -> str:
    """ This function would pass the 79 character limit.
    """
    return f"{first_argument} {second_argument}"


def fifth_function_with_very_long_name(first_argument: str,
                                       second_argument: int) -> str:
    """ This function would pass the 79 character limit.
    """
    return f"{first_argument} {second_argument}"


def function_with_math_operators(
        first_long_argument, second_long_argument,
        third_long_argument, fourth_long_argument):
    """ This function content would pass the 79 character limit.
    """
    # It is recommended that we break we place the math operators at the
    # beginning of the line, not at the end of the line.
    return (first_long_argument
            + second_long_argument
            - third_long_argument
            * fourth_long_argument)


def function_example_with_backslash(number_to_check):
    """ This function content would pass the 79 character limit.
    """
    return number_to_check < 10 or 21 <= number_to_check < 20 or \
        number_to_check > 100


def function_with_if_examples(number_to_check):
    """ This function content would pass the 79 character limit.
    """
    # Notice that the conditions aren't at the same level of parenthesis
    if (
            number_to_check < 10 or
            21 <= number_to_check < 20 or
            number_to_check > 100):
        return True
    # Notice that the closing parenthesis is at the same level of the oppening
    # parenthesis
    if (
            number_to_check < 10 or
            21 <= number_to_check < 20 or
            number_to_check > 100
       ):
        return True
    # Notice that the closing parenthesis is at the same level of the if clause
    if (
            number_to_check < 10 or
            21 <= number_to_check < 20 or
            number_to_check > 100
    ):
        return True
    # This is my least preferred one
    if (number_to_check < 10 or
            21 <= number_to_check < 20 or
            number_to_check > 100):
        return True


# This is an example of a long string
LONG_STRING = ("This is an example of a very long Python string. We can use "
               "parenthesis, and single or double quotes for that."
               )


# This is an example of a long string using f-strings
a_value = input()
long_fstring = ("This is an example of a very long Python string. We can use "
                f"parenthesis, and single or double quotes for that. {a_value}"
                )
