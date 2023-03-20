""" This module shows Python example of how to reduce if statement
"""


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
    # We can also use variables to store conditions
    oil_level_above_minimum = oil_level > 3
    fuel_level_above_minimum = fuel_level > 5
    if (
            oil_level_above_minimum
            and fuel_level_above_minimum
       ):
        return True
    return False
