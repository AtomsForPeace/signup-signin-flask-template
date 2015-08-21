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
    ctime = db.Column('ctime', db.DateTime)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email.lower()
        self.set_password(password)
        self.ctime = datetime.utcnow()

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        try:
            return unicode(self.uid)
        except NameError:
            return str(self.uid)
