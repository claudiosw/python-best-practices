""" This file has fixtures for the tests included in this directory
"""


import uuid
from datetime import datetime
import pytest
from testing.pytesting import Product


@pytest.fixture(autouse=True)
def time_calculator():
    """ Example of an autouse fixture """
    # To see this, execute pytest with "-s" option
    print(f" Test started: {datetime.now().strftime('%d-%m-%Y %H:%M')} ")
    yield
    print(f" Test ended: {datetime.now().strftime('%d-%m-%Y %H:%M')} ")


@pytest.fixture()
def fixture_product_1():
    """ Example of a fixture of one product """
    return Product(
        id=uuid.uuid4(),
        price=1.11,
        name="test 1"
    )


@pytest.fixture()
def fixture_product_2():
    """ Example of a fixture of another product """
    return Product(
        id=uuid.uuid4(),
        price=11,
        name="test 2"
    )


@pytest.fixture()
def product_fixture_list(fixture_product_1, fixture_product_2):
    """ Example of a fixture composed of two other fixtures """
    return [fixture_product_1, fixture_product_2]
