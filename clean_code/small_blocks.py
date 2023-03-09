""" This module shows Python small block best practice examples
"""

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

    def calculate_price_before_tax(self):
        """ This method calculates the price before tax
        """
        return self.cost_price * (1 + DEFAULT_MARGIN_PERCENT / 100)

    def calculate_taxes_percent(self):
        """ This method calculates the taxes in percent
        """
        if self.imported:
            return DEFAULT_TAX + DEFAULT_IMPORT_TAX
        else:
            return DEFAULT_TAX

    def calculate_sale_price(self):
        """ This method calculates the sale price of the car
        """
        return (self.calculate_price_before_tax()
                * (1 + self.calculate_taxes_percent() / 100))


# Long if example
def is_car_ok_long(oil_level, fuel_level, right_door_status, left_door_status):
    """ This method checks the car status
    """
    if (
            oil_level > 3
            and fuel_level > 5
            and right_door_status == "closed"
            and left_door_status == "closed"
       ):
        return True
    return False


# Shorter if example using functions and variables
def is_car_ok(oil_level, fuel_level, right_door_status, left_door_status):
    """ This method checks the car status
    """
    if (
            is_car_levels_ok(oil_level, fuel_level)
            and is_car_doors_closed(right_door_status, left_door_status)
       ):
        return True
    return False


def is_car_doors_closed(right_door_status, left_door_status):
    """ This method checks the car doors status
    """
    if (
            right_door_status == "closed"
            and left_door_status == "closed"
       ):
        return True
    return False


def is_car_levels_ok(oil_level, fuel_level):
    """ This method checks the car levels status
    """
    # We can also use variable to store conditions
    oil_level_above_minimum = oil_level > 3
    fuel_level_above_minimum = fuel_level > 5
    if (
            oil_level_above_minimum
            and fuel_level_above_minimum
       ):
        return True
    return False
