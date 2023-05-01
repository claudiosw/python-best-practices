""" Tests restated to Pytest """


import pytest
from .pytesting import add, get_user_inputs, print_hello_world_with_error


def test_add():
    """ Doing simple tests """
    assert add(1, 2) == 3
    assert add(1, 2) < 4


def test_product_list(product_fixture_list):
    """ Test example using fixture """
    assert len(product_fixture_list) == 2
    assert add(
                product_fixture_list[0].price,
                product_fixture_list[1].price
           ) == 12.11


@pytest.mark.parametrize("parameter_1, parameter_2, expected_result", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 1, 1)])
def test_add_parametrize(parameter_1, parameter_2, expected_result):
    """ Test example using parametrize feature of Pytest """
    assert add(parameter_1, parameter_2) == expected_result


def test_stdout_stderr(capsys):
    """ Test example using capsys to test stdout and stderr """
    print_hello_world_with_error()
    captured = capsys.readouterr()
    # Asserting that the captured standard output (print) is what we expect
    # Notice that print adds a newline (/n) at the end of the string
    assert captured.out == "Hello World\n"
    # Asserting that the captured standard error (sys.stderr.write) is what we
    # expect
    assert captured.err == "This is an error"


def test_user_input(monkeypatch):
    fake_user_input1 = "This is the first user input"
    fake_user_input2 = 42
    fake_user_inputs = iter([fake_user_input1, str(fake_user_input2)])
    # This simulates user inputs in the terminal, each input as one variable:
    monkeypatch.setattr('builtins.input', lambda _: next(fake_user_inputs))
    # Printing and generating error:
    received_user_inputs = get_user_inputs()
    # Asserting that the received user inputs are what we expect
    assert received_user_inputs["user_input1"] == fake_user_input1
    assert received_user_inputs["user_input2"] == str(fake_user_input2)
