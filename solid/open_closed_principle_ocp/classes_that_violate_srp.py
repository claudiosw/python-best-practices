""" This module has example of Open/Closed Principle in Python where Classes
    DON'T follow the Single Responsibility Principle
"""


# This UserBad class is not following the Open/Closed Principle because if
# we need to add a responsibility, we would need to modify the class.
# For example, if we add the feature of sending email like the example shown on
# the SRP example, we need to modify the UserBad class.
class UserBad():
    """ This is an example of a class in Python that is NOT following the
        Single Responsibility Principle and Open/Closed Principle
    """
    def __init__(self, username, name):
        self.username = username
        self.name = name

    def save(self):
        """ This method would send confirmation email
        """
        print("Saving data into database")


# Here we separated the responsibilities, each responsibility in your
# respective class. So, this example follows the Open/Closed Principle and
# Single Responsibility Principle. Before, we had two reasons to change the
# UserBad class, changing user properties and saving to database. Now, each of
# these has its own class and if we need an additional responsibility, we would
# create a new class.
class User():
    """ This class is an example of Open/Closed Principle in Python
    """
    def __init__(self, username, name):
        self.username = username
        self.name = name


class UserDatabase():
    """ This class is an example of Open/Closed Principle in Python
    """
    def save(self, user: User):
        """ This method would save data to the database
        """
        print(f"Saving {user} to database")
