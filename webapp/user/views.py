from flask_login import current_user, login_user, logout_user
from flask import Blueprint, render_template, flash, redirect, url_for

from webapp.user.forms import LoginForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('user/login.html', page_title = title, form = login_form)

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт!')
            return redirect(url_for('news.index'))
    flash('No corret User or Password')
    return redirect(url_for('user.login'))

@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Вы вышли!')
    return redirect(url_for('news.index'))
