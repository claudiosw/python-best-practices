""" This module shows StepDown Rule Python example
"""


DEFAULT_MARGIN_PERCENT = 50
DEFAULT_IMPORT_TAX = 10
DEFAULT_TAX = 10


# This example is NOT following the StepDown Rule example because the highest
# level of abstraction is at the bottom of the class.
class ElectricCarEvenShorterVersion():
    """ This is a class example to show naming best practices
    """
    def __init__(self, name, cost_price, imported) -> None:
        self.name = name
        self.cost_price = cost_price
        self.imported = imported

    def __calculate_price_before_tax(self):
        """ This method calculates the price before tax
        """
        return self.cost_price * (1 + DEFAULT_MARGIN_PERCENT / 100)

    def __calculate_taxes_factor(self):
        """ This method calculates the taxes in percent
        """
        if self.imported:
            taxes_percent = DEFAULT_TAX + DEFAULT_IMPORT_TAX
        else:
            taxes_percent = DEFAULT_TAX
        return 1 + taxes_percent / 100

    def calculate_sale_price(self):
        """ This method calculates the sale price of the car
        """
        return (self.__calculate_price_before_tax()
                * self.__calculate_taxes_factor())


# This rule states that when we read a code, the higher level of abstraction
# should be at the top of the file, not at the bottom. So, in the previous
# code, the calculate_sale_price method should be at the top of the class like
# this:
class ElectricCarStepDownRule():
    """ This is a class example to show naming best practices
    """
    def __init__(self, name, cost_price, imported) -> None:
        self.name = name
        self.cost_price = cost_price
        self.imported = imported

    def calculate_sale_price(self):
        """ This method calculates the sale price of the car
        """
        return (self.__calculate_price_before_tax()
                * self.__calculate_taxes_factor())

    def __calculate_price_before_tax(self):
        """ This method calculates the price before tax
        """
        return self.cost_price * (1 + DEFAULT_MARGIN_PERCENT / 100)

    def __calculate_taxes_factor(self):
        """ This method calculates the taxes in percent
        """
        if self.imported:
            taxes_percent = DEFAULT_TAX + DEFAULT_IMPORT_TAX
        else:
            taxes_percent = DEFAULT_TAX
        return 1 + taxes_percent / 100
