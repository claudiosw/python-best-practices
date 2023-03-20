""" This module shows Python small block best practice example
"""
# Try to write small functions/methods that do one thing and one thing well.
# They should hardly ever be 20 lines long and the ideal goal would be less
# than 5 lines. Having small code blocks and each one having a name helps to
# have cleaner code that is easier to understand.


DEFAULT_MARGIN_PERCENT = 50
DEFAULT_IMPORT_TAX = 10
DEFAULT_TAX = 10


# This example show a method that could be smaller
class ElectricCarLongVersion():
    """ This is a class example to show naming best practices
    """
    def __init__(self, name, cost_price, imported) -> None:
        self.name = name
        self.cost_price = cost_price
        self.imported = imported

    def calculate_sale_price(self):
        """ This method calculates the sale price of the car
        """
        price_before_tax = self.cost_price * (1 + DEFAULT_MARGIN_PERCENT / 100)
        if self.imported:
            taxes_percent = DEFAULT_TAX + DEFAULT_IMPORT_TAX
        else:
            taxes_percent = DEFAULT_TAX
        return price_before_tax * (1 + taxes_percent / 100)


# This example show shorter methods
class ElectricCarShortVersion():
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
