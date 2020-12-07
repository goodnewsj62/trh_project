from trh_app import db
from flask_login import UserMixin


class Records(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    sex = db.Column(db.String(15), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(14), nullable=False)
    day = db.Column(db.String(20), nullable=False)
    seat = db.Column(db.Integer, nullable=False)


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
