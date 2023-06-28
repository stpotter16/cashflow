"""Cashflow: See where your money is and where it is going."""
import os
from typing import Any, Literal, Mapping

from flask import Flask

__version__ = "0.1.0"


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    """Application factory.

    Creates an instance of the Flask application.

    Args:
        test_config: An optional dict containing configuration options for
            unit tests.

    Returns:
        An instance of a Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        DATABASE=os.path.join(app.instance_path, "cashflow.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello() -> Literal["Hello, World!"]:
        return "Hello, World!"

    return app
