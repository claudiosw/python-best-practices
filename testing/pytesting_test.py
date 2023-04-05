""" Tests restated to Pytest """


import pytest
from .pytesting import add


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
