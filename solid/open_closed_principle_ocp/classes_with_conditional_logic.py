""" This module has example of Open/Closed Principle in Python where Classes
    have conditional logic
"""
from abc import ABC, abstractmethod


class InterestRateBadExample():
    """ This is an example of a class in Python that is NOT following the
        Open/Closed Principle
    """
    def get_interest_rate(self, category):
        """ Method to get interest rate
        """
        if category == 'standard':
            return 0.03
        elif category == 'premium':
            return 0.05


class InterestRate(ABC):
    """ This is an example of an abstract class in Python that is following the
        Open/Closed Principle
    """
    @abstractmethod
    def get_interest_rate(self):
        """ Method to get interest rate
        """


class StandardInterestRate(InterestRate):
    """ This is an example of a class in Python that is following the
        Open/Closed Principle
    """
    def get_interest_rate(self):
        """ Method to get interest rate
        """
        return 0.03


class PremiumInterestRate(InterestRate):
    """ This is an example of a class in Python that is following the
        Open/Closed Principle
    """
    def get_interest_rate(self):
        """ Method to get interest rate
        """
        return 0.05
