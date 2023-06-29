from typing import Literal

from flask import Blueprint

bp = Blueprint("timeline", __name__)

@bp.route("/")
def index() -> Literal["Hello, World!"]:
    return "Hello, World!"
