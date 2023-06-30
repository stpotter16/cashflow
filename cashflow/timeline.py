"""Timeline views."""
from flask import Blueprint, render_template

bp = Blueprint("timeline", __name__)


@bp.route("/")
def index() -> str:
    """Timeline view.

    This route displays the money timeline.

    Returns:
        String
    """
    return render_template("timeline.html")
