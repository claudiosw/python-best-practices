""" This module has an example of the Open/Close Principle in Python where
    classes are tightly coupled.
"""


class UserBadExample():
    """ This is an example of a class in Python that is NOT following the
        Open/Closed Principle
    """
    def __init__(self, username, name):
        self.username = username
        self.name = name


# This function is tightly coupled to the UserBadExample class as we would need
# to change the get_user_bad_example function if we need to change the
# UserBadExample class. That also violates the Open/Close Principle.
def get_user_bad_example(user_bad_example):
    """ This is an example of a Python function that is NOT following the
        Open/Closed Principle
    """
    return {
                "username": user_bad_example.username,
                "name": user_bad_example.name
           }


# Transforming the function into a method of the class solves the previous
# problem and follows the Open/Close Principle.
class User():
    """ This is an example of a Python class that follows the
        Open/Closed Principle
    """
    def __init__(self, username, name):
        self.username = username
        self.name = name

    def get(self):
        """ Get user data """
        return {"username": self.username, "name": self.name}
