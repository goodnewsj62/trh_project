from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, RadioField, SelectField, PasswordField
from wtforms.validators import ValidationError, Length, DataRequired
from trh_app.model import Records


class LoginForm(FlaskForm):
    username = StringField('username', validators=[
                           Length(min=4, max=25), DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember me')
    submit = SubmitField('Login')
