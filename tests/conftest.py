"""Test fixtures."""
from collections.abc import Generator
from typing import Any

from flask import Flask
from flask.testing import FlaskClient
import pytest

from cashflow import create_app


@pytest.fixture
def app() -> Generator[Flask, Any, Any]:
    """Application for testing.

    Creates an instance of a Flask application for testing.

    Returns:
        An instance of a Flask app
    """
    app = create_app({"TESTING": True})

    yield app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """Client for application testing.

    Creates an instance of a FlaskClient for application testing.

    Args:
        app: The test flask application that the client interacts with

    Returns:
        An instance of a test client
    """
    return app.test_client()
