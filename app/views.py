from app import app, login_manager
from flask import (render_template, redirect, request,
    abort, url_for, session, g)
from flask.ext.login import (
    login_user, logout_user, current_user, login_required,
    AnonymousUserMixin)

from .forms import SignupForm, SigninForm
from .models import db, User


login_manager.login_view = 'signin'


def create_new_user(form_data):
    newuser = User(
        form_data.username.data,
        form_data.email.data,
        form_data.password.data)
    db.session.add(newuser)
    db.session.commit()
    login_user(newuser)


@app.before_request
def before_request():
    g.user = current_user


@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print(g.user)
    if g.user.is_authenticated():
        return redirect(url_for('index'))
    form = SignupForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:
            create_new_user(form)

            return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('signup.html', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if g.user.is_authenticated():
        return redirect(url_for('index'))
    form = SigninForm()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('signin.html', form=form)
        else:
            registered_user = User.query.filter_by(
                email=form.email.data).first()
            login_user(registered_user)
            return redirect(url_for('index'))

    elif request.method == 'GET':
        return render_template('signin.html', form=form)


@app.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('signin'))
