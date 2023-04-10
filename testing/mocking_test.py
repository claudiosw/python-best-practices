""" Tests to demonstrate testing.
"""


import unittest
from unittest.mock import Mock, patch
from testing import mocking


def test_mock_function():
    """ Test that a mock function is called
    """
    object_to_mock = Mock()
    object_to_mock.method_example("parameter example")

    assert object_to_mock.method_example.call_count == 1

    object_to_mock.method_example.assert_called()
    object_to_mock.method_example.assert_called_once()
    object_to_mock.method_example.assert_called_with("parameter example")
    object_to_mock.method_example.assert_called_once_with("parameter example")

    object_to_mock.method_example()

    assert object_to_mock.method_example.call_count == 2

    object_to_mock.method_example.assert_called_with()


class TestRunDice(unittest.TestCase):
    """ Tests for the run_dice function isolating it from random library
    """
    # With @patch("testing.mocking.random"), we mock random from the mocking.py
    # file which is the file where the function run_dice is located.
    @patch("testing.mocking.random")
    # The mock_random parameter of the test_mock_function_with_dice method is
    # the name of the mock object we pass to the test method.
    def test_mock_function_with_dice(self, mock_random):
        """ Testing run_dice function
        """
        # We say randint should return 4 then we execute the run_dice function.
        mock_random.randint.return_value = 4

        # Testing if run_dice returns "Lucky".
        assert mocking.run_dice() == "Lucky"

        # We say that randint should return 3.
        mock_random.randint.return_value = 3

        # We execute the run_dice function and test if it returns "Unlucky".
        assert mocking.run_dice() == "Unlucky"
