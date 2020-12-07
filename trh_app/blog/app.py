from flask import request, url_for, abort, render_template, flash, redirect, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from .form import RegisterForm
from trh_app.model import Records, db


blog = Blueprint('blog', __name__)


@blog.route('/')
@blog.route('/home')
def home():
    return render_template('blog/home.html')


@blog.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        result = Records.query.filter_by(day=form.day.data).all()
        result = [each.seat for each in result]

        if form.seat_no.data in result:
            flash('Seat number is taken')
        else:
            record = Records(name=form.name.data, sex=form.sex.data,
                             status=form.status.data, phone=form.phone_no.data, day=form.day.data, seat=form.seat_no.data)
            db.session.add(record)
            db.session.commit()

            flash(f'Congrats {form.name.data} your reservation has been made')
            return redirect(url_for('blog.done'))
    return render_template('blog/register.html', form=form)


@blog.route('/done', methods=['GET'])
def done():
    return render_template('blog/done.html')
