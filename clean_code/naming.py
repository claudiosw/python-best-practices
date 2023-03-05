""" This module shows Python naming best practice examples
"""

# Notice that the constant name is self explanatory and is a noun.
# Don't try to cut back letters like DEF_MARG_PERC or DMP
DEFAULT_MARGIN_PERCENT = 50


class ElectricCar():
    """ This is a class example to show naming best practices
        Notice that the class is named as a noun, not a verb.
        Following PEP8 naming convention, it uses camel case.
    """
    def __init__(self, name, cost_price) -> None:
        self.name = name
        self.cost_price = cost_price

    def calculate_sale_price(self):
        """ This method calculates the sale price of the car
            Notice that the method is named as a verb.
            Following PEP8, it's name uses lowercases and underscores.
        """
        # Notice that the constant DEFAULT_MARGIN_PERCENT helps to understand
        # the calculation logic. If we use 50 instead, 50 would be a magic
        # number and it would be more difficult to understand.
        return self.cost_price * (1 + DEFAULT_MARGIN_PERCENT / 100)

    def get_name(self):
        """ This method returns the name of the car
        """
        return self.name

    def get_cost_price(self):
        """ This method returns the cost price of the car
            Notice that both get_name and get_cost_price use the same verb.
            We should not name them get_name and fetch_cost_price, for instance
        """
        return self.cost_price


def explode_word(word):
    """ This function is a function to explode a word
        Notice that the function is named as a verb.
        Following PEP8, it's name uses lowercases and underscores.
    """
    # We could name character as i in loops. But character is probably clearer.
    for character in word:
        print(character)
