"""Tests timeline page."""


from flask.testing import FlaskClient


def test_index(client: FlaskClient) -> None:
    """Test index page contents."""
    response = client.get("/timeline")
    assert b"Menu" in response.data
    assert b"Cashflow" in response.data
    assert b"Log out" in response.data
    assert b"Timeline" in response.data
    assert b"Date" in response.data
    assert b"Name" in response.data
    assert b"Amount" in response.data
    assert b"Account" in response.data
    assert b"Category" in response.data
