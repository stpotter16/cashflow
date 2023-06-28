"""Test application factory."""
from cashflow import create_app


def test_config() -> None:
    """Test configuration settings are registered by the app."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing
