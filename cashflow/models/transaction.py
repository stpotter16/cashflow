"""Database model for transaction."""
from cashflow import db


class Transaction(db.Model):
    """Transaction data model.

    Represents the database schema for a transaction.
    """

    id = db.Column(db.String, primary_key=True)
    date = db.Column(db.DateTime)
    name = db.Column(db.String, nullable=True)
    amount = db.Column(db.Numeric, nullable=True)
    account = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=True)
