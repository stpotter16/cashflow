"""Flow view."""
from datetime import datetime
from uuid import uuid4

from flask import Blueprint, redirect, Response, render_template

from cashflow import db
from cashflow.models.flow import Flow

bp = Blueprint("flow", __name__)


@bp.route("/flow", methods=["POST"])
def flow_new() -> Response:
    """Flow form processing.

    This route handles creating a new flow.

    Returns:
        Response
    """
    id = str(uuid4())
    flow = Flow(id=id, created=datetime.now())
    db.session.add(flow)
    db.session.commit()
    response = redirect(f"/transaction/{id}", 302)
    return response


@bp.route("/flow/<id>")
def flow(id: str) -> str:
    """Flow view.
    
    This route handles the view of a flow.

    Returns:
        String
    """
    return render_template("flow.html")
