""" This module has an example of the Liskov Substitution Principle(LSP) in
    Python.
"""


# The example below violates The Liskov Substitution Principle as the calculate
# Father class returns a value and the method from SonBadExample class prints
# it.
class Father():
    """ Example of a base class
    """
    def add(self, first: float, second: float) -> float:
        """ Do a calculation
        """
        return first + second


class SonBadExample(Father):
    """ Example of a child class that violates the Liskov Substitution
        Principle
    """
    def add(self, first: float, second: float) -> None:
        """ Do a calculation
        """
        print(first + second)


# On the other hand, the class below doesn't do polymorphism but creates a new
# method which follows the Liskov Substitution Principle.
class Son(Father):
    """ Example of a child class that follows the Liskov Substitution Principle
    """
    def print_addition(self, first: float, second: float) -> None:
        """ Do a calculation
        """
        print(self.add(first, second))
