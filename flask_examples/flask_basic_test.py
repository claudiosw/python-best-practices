""" Basic Flask Example Test
"""


import pytest
from flask_basic import create_basic_flask_app


@pytest.fixture()
def app_flask():
    """ Instance Basic Flask App to test
    """
    app = create_basic_flask_app()
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture()
def client(app_flask):
    """ Client test for Basic Flask App
    """
    return app_flask.test_client()


def test_request_example(client):
    """ Test request example
    """
    response = client.get("/")
    assert b"Hello World!" in response.data
