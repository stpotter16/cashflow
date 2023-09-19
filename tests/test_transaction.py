"""Tests transaction page."""


from flask import Flask
from flask.testing import FlaskClient


def test_transaction_get(client: FlaskClient) -> None:
    """Test transaction page contents."""
    response = client.get("/transaction")
    assert b"Menu" in response.data
    assert b"Cashflow" in response.data
    assert b"Log out" in response.data
    assert b"Add Transaction" in response.data
    assert b"Date" in response.data
    assert b"Name" in response.data
    assert b"Amount" in response.data
    assert b"Account" in response.data
    assert b"Category" in response.data


def test_transaction_post(client: FlaskClient, app: Flask) -> None:
    """Test transaction post action."""
    # TODO - This is just a smoke test for place-holding
    client.post("/transaction")
