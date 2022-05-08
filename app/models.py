from enum import unique
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    points = db.Column(db.Integer)
    soc = db.Column(db.Integer)

    def __repr__(self) -> str:
        return "<User {}>".format(self.username)