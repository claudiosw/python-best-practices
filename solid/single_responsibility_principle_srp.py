""" This module has examples of the Single Responsibility Principle in Python
"""


# This UserBad class is not following the Single Responsibility Principle as it
# has two responsibilities: managing user properties and sending confirmation
# email.
class UserBad():
    """ This is an example of a class in Python that is NOT following the
        Single Responsibility Principle
    """
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address
        self.send_confirmation_email()

    def send_confirmation_email(self):
        """ This method would send confirmation email
        """
        print(f"Sending confirmation email to {self.email_address}")


# Here we separated the responsibilities, each responsibility in your
# respective class. So, this example follows the Single Responsibility
# Principle. Before, we had two reasons to change the UserBad class, changing
# user properties and changing how the email is sent. Now, each of these has
# its own class.
class User():
    """ This class is an example of the Single Responsibility Principle in Python
    """
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address
        self.email = Email(email_address)
        self.email.send_confirmation_email()


class Email():
    """ This class is an example of the Single Responsibility Principle in Python
    """
    def __init__(self, email_address):
        self.email_address = email_address

    def send_confirmation_email(self):
        """ This method would send confirmation email
        """
        print(f"Sending confirmation email to {self.email_address}")
