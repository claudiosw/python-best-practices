""" This is a Python module example to show PEP 8 blank lines code layout.
"""

# importing os module
import os


class CurrentDirectory:
    """ This is a class example that shows the current directory
        See that there are two blank lines before a class
    """
    def __init__(self) -> None:
        self.current_directory = os.getcwd()

    def show_directory(self):
        """ This is a method example that shows the current directory
            See that there is only one blank line before a method
        """
        return self.current_directory

    def list_directory(self):
        """ This is a method example that lists the current directory
        """
        directory_listing = os.listdir(self.current_directory)

        # This blank line above is optional.
        # We can use these optional blank lines to organize the code.
        return directory_listing


def top_level_function():
    """ This is a function example of a top level function.
        See that there are two blank lines before a top level function
    """
    return None
