"""Timeline views."""
from typing import Literal

from flask import Blueprint

bp = Blueprint("timeline", __name__)


@bp.route("/")
def index() -> Literal["Hello, World!"]:
    """Timeline view.

    This route displays the money timeline.

    Returns:
        String
    """
    return "Hello, World!"
