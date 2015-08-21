from datetime import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    __tablename__ = "users"
    uid = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(20), unique=True, index=True)
    email = db.Column('email', db.String(120), unique=True)
    pwdhash = db.Column('password', db.String(54))
    ctime = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
