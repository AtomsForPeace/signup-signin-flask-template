from flask import g
from flask_wtf import Form
from wtforms import (
    TextField, SubmitField, validators, ValidationError,
    PasswordField)
from .models import db, User


class SignupForm(Form):
    username = TextField(
        'username',
        [validators.Required("Please enter a username")])
    email = TextField(
        'email',
        [validators.Required("Please enter an email address"),
        validators.Email("Please enter your email address.")])
    password = PasswordField(
        'password',
        [validators.Required("Please enter a password")])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(
            email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            g.user = user
            return True


class SigninForm(Form):
    email = TextField(
        'email',
        [validators.Required("Please enter a email")])
    password = PasswordField(
        'password',
        [validators.Required("Please enter a password")])
    submit = SubmitField("Sign In")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(
            email=self.email.data.lower()).first()
        if user and user.check_password(self.password.data):
            g.user = user
            return True
        else:
            self.email.errors.append("Invalid email or password")
            return False
