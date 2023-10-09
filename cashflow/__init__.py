"""Cashflow: See where your money is and where it is going."""
import os
from typing import Any, Mapping

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__version__ = "0.1.0"

# TODO - I hate that this is global
db = SQLAlchemy()


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

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            DATABASE=os.path.join(app.instance_path, "cashflow.sqlite"),
            SQLALCHEMY_DATABASE_URI="sqlite:///cashflow.sqlite",
        )
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    import cashflow.models  # noqa: F401

    with app.app_context():
        db.create_all()

    from .views import flow, landing, timeline, transaction

    app.register_blueprint(flow.bp)
    app.register_blueprint(landing.bp)
    app.register_blueprint(timeline.bp)
    app.register_blueprint(transaction.bp)
    app.add_url_rule("/", endpoint="landing")

    return app
