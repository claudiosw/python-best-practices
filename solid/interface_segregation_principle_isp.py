""" This module has examples of the Interface Segregation Principle (ISP)
    in Python.
"""


from abc import ABC, abstractmethod


class EmployeeBadExample(ABC):
    """ An abstract class example that doesn't follow the Interface Segregation
        Principle as it has methods that aren't used by its child classes
    """

    @abstractmethod
    def write_code(self):
        """ Write code method
        """

    @abstractmethod
    def cook(self):
        """ Cook method
        """

    @abstractmethod
    def lead(self):
        """ Lead method
        """


class ChefBadExample(EmployeeBadExample):
    """ Chef Class
    """
    def write_code(self):
        raise NotImplementedError("Chefs don't write code.")

    def cook(self):
        print("I am cooking")

    def lead(self):
        print("I am leading")


# Those classes from now on follow the Interface Segregation Principle
# Instead of having one abstract class for all employees, we divided them by
# roles and the child class uses multiple inheritance.
# If you don’t know what multiple inheritance is, the Chef class has multiple
# inheritance as it has two parent classes. Chef class inherits the lead method
# from the Leader class and the cook method from the Cook class.
class Cook(ABC):
    """ An abstract class representing a cook (person who cooks)
    """
    @abstractmethod
    def cook(self):
        """ Cook method

        """


class Leader(ABC):
    """ An abstract class representing a leader
    """

    @abstractmethod
    def lead(self):
        """ Lead method
        """


class Chef(Cook, Leader):
    """ Chef Class
    """
    def lead(self):
        print("I am leading")

    def cook(self):
        print("I am cooking")


# Alternatively, the method could be implemented directly on the child class
# without relating it to the parent class. The fly method of the Bird class
# below is an example of this approach.
class Animal(ABC):
    """ An abstract class representing a leader
    """

    @abstractmethod
    def eat(self):
        """ Eat method
        """


class Bird(Animal):
    """ Bird Class
    """
    def eat(self):
        print("I am eating")

    def fly(self):
        """ Fly method
        """
        print("I am flying")
