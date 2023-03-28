""" This class is an example on how to document Python code
"""

def transform_int_to_str (number: int) -> str:
    """ Transform a int to a string

    :param number: number to transform
    :returns: A string with 'The input was ' concatenated with the parameter
    """
    return f"The input was {number}"


class Transformer():
    """
    Small description of the class

    Larger description of the class. This class is just an example to show how
    to document Python code.
    """
    def transform_float_less_than_100_to_int (self, number: float) -> int:
        """ Transform a number to string

        :param number: number to transform
        :raises ValueError: if the parameter is greater or equal to 100
        :returns: A string with 'The input was ' concatenated with the
        parameter
        """
        if number < 100:
            return int(number)
        else:
            raise ValueError(f"{number} is greater or equal to 100")
