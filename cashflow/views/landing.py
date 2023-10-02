"""Home view."""
from flask import Blueprint, render_template

bp = Blueprint("landing", __name__)


@bp.route("/")
def landing() -> str:
    """Home view.

    This route displays the landing view.

    Returns:
        String
    """
    return render_template("landing.html")
