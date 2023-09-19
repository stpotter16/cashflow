"""Test application factory."""
import os
import tempfile

from cashflow import create_app


def test_config() -> None:
    """Test configuration settings are registered by the app."""
    assert not create_app().testing

    db_fd, db_path = tempfile.mkstemp()
    app = create_app(
        {
            "TESTING": True,
            "DATABASE": db_path,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///cashflow.sqlite",
        }
    )
    assert app.testing

    os.close(db_fd)
    os.unlink(db_path)
