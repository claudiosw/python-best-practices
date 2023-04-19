""" In this file we have tests that use pytest-mock
"""
from testing import mocking
from testing.mocking import ExampleRepositoryInterface


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


def test_create_example(mocker):
    """ Example of a test passing a mock as a parameter
    """
    # Mocking the object
    repository_mock = mocker.patch.object(
        ExampleRepositoryInterface,
        "create"
    )
    # Defining the result it will return
    repository_mock.create.return_value = "Result Example created"
    # Executing the test
    use_case = mocking.CreateExampleUseCase(repository_mock)
    result = use_case.execute("Name Example")
    # Check if the mocked method of the object received the correct parameter
    repository_mock.create.assert_called_once_with("Name Example")
    # Check if the use case passed the result of the mocked object correctly
    assert result == "Result Example created"
