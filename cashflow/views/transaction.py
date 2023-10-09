"""Transaction routes."""
from datetime import datetime
from uuid import uuid4

from flask import Blueprint, redirect, render_template, request, Response

from cashflow import db
from cashflow.models.transaction import Transaction

bp = Blueprint("transaction", __name__)


@bp.route("/flow/<flowid>/transaction", methods=["GET"])
def flow_transaction_get(flowid: str) -> str:
    """Transaction for particular flow form view.

    This route displays the form to add a transaction to a particular flow.

    Returns:
        String
    """
    return render_template("flow_transaction.html")


@bp.route("/transaction", methods=["GET"])
def transaction_get() -> str:
    """Transaction form view.

    This route displays the form to add a transaction.

    Returns:
        String
    """
    return render_template("transaction.html")


@bp.route("/transaction", methods=["POST"])
def transaction_post() -> Response:
    """Transaction form processing.

    This route handles posts from the transaction form.

    Returns:
        Response
    """
    transaction_data = request.form
    transaction = Transaction(
        id=str(uuid4()),
        date=datetime.fromisoformat(transaction_data["date"]),
        name=transaction_data["name"],
        amount=transaction_data["amount"],
        account=transaction_data["account"],
        category=transaction_data["category"],
    )
    db.session.add(transaction)
    db.session.commit()
    response = redirect("/", code=302)
    return response
