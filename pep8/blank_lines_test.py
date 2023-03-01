""" Tests for blank_lines module
"""

# importing os module
import os
from blank_lines import CurrentDirectory


def test_current_directory():
    """ Test for CurrentDirectory class
    """
    current_directory = CurrentDirectory()

    assert current_directory.show_directory() == os.getcwd()
