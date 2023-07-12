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
    transactions = [
        {
            "date": "2023-07-07",
            "name": "Publix",
            "amount": 100.00,
            "account": "Checking",
            "category": "Groceries",
        },
        {
            "date": "2023-07-07",
            "name": "Chick-fil-a",
            "amount": 25.00,
            "account": "Credit Card",
            "category": "Resturants",
        },
    ]
    return render_template("timeline.html", transactions=transactions)
