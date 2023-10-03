"""Database model for cashflow."""
from cashflow import db


class Flow(db.Model):
    """Flow data model.

    Represents the database schema for a flow.
    """

    __tablename__ = "Flow"
    id = db.Column(db.String, primary_key=True)
    created = db.Column(db.DateTime)
    name = db.Column(db.String, nullable=True)
