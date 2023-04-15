""" In this file we have tests that use pytest-mock
"""
from testing import mocking


def test_mock_patch_function_with_dice(mocker):
    """ Testing run_dice function
    """
    # We say randint should return 4 then we execute the run_dice function.
    mocker.patch(
        # api_call is from slow.py but imported to main.py
        'testing.mocking.random.randint',
        return_value=4
    )
    # Testing if run_dice returns "Lucky".
    assert mocking.run_dice() == "Lucky"
    assert mocking.random.randint.call_count == 1  # pylint: disable=E1101
    assert mocking.random.randint.call_once_with(1, 6)  # pylint: disable=E1101
    assert mocking.random.randint.call_with(1, 6)  # pylint: disable=E1101

    # We say randint should return 3 then we execute the run_dice function.
    mocker.patch(
        # api_call is from slow.py but imported to main.py
        'testing.mocking.random.randint',
        return_value=3
    )
    # Testing if run_dice returns "Unlucky".
    assert mocking.run_dice() == "Unlucky"
    assert mocking.random.randint.call_count == 1  # pylint: disable=E1101
    assert mocking.random.randint.call_with(1, 6)  # pylint: disable=E1101

    assert mocking.run_dice() == "Unlucky"
    assert mocking.random.randint.call_count == 2  # pylint: disable=E1101
    # We disable the E1101 pylint message because pylint can't figure out what
    # mock is doing behind the scene in a sane way.This problem only occurs
    # when you're mocking a module. Pylint correctly finds the type of the mock
    # if you're mocking a function, class or method.
