"""Test fixtures."""
from collections.abc import Generator
import os
import tempfile
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
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(
        {
            "TESTING": True,
            "DATABASE": db_path,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///cashflow.sqlite",
        }
    )

    yield app

    os.close(db_fd)
    os.unlink(db_path)


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
