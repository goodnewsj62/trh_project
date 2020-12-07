from flask import request, url_for, abort, render_template, flash, redirect, Blueprint, session
from .form import LoginForm
from trh_app.model import Records, Admin
from trh_app import db, login_manager, bcrypt_
from flask_login import login_required, login_user, logout_user, current_user
from functools import wraps
import pandas as pd


auth = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)


def check_authenticated(func):
    @wraps(func)
    def redirect_wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return func(*args, **kwargs)
        return redirect(url_for('auth.admin_page'))
    return redirect_wrapper


@auth.route('/login', methods=['GET', 'POST'])
@check_authenticated
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(username=form.username.data).first()

        if user and bcrypt_.check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            login_user(user, remember=form.remember.data)
            flash('You have logged in successfully')
            next = request.args.get('next')

            if next:
                try:
                    return redirect(next)
                except:
                    return redirect(url_for('auth.admin_page'))
            else:
                return redirect(url_for('auth.admin_page'))
        else:
            flash('Wrong password or username')

    return render_template('admin/login.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear
    logout_user()
    flash('you have logged out successfully')
    return redirect(url_for('auth.login'))


@auth.route('/admin', methods=['GET', 'POST'])
@login_required
def admin_page():
    total_registered = Records.query.count()
    all_records = Records.query.all()

    return render_template('admin/admin.html', file=all_records, count=total_registered)
