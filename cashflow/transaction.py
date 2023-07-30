"""Transaction routes."""
from flask import Blueprint, render_template

bp = Blueprint("transaction", __name__)


@bp.route("/transaction", methods=["GET"])
def transaction() -> str:
    """Transaction form view.

    This route displays the form to add a transaction.

    Returns:
        String
    """
    return render_template("transaction.html")
