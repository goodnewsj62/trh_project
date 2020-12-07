from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, IntegerField, RadioField, SelectField, PasswordField
from wtforms.validators import ValidationError, Length, DataRequired
from trh_app.model import Records


class RegisterForm(FlaskForm):

    name = StringField('full name', validators=[
        DataRequired(), Length(min=4, max=25)])

    sex = RadioField('gender', choices=[
                     ('male', 'male'), ('female', 'female')], validators=[DataRequired()])

    status = SelectField('relationship status', choices=[
                         ('single', 'single',), ('married', 'married',)], validators=[DataRequired()])

    phone_no = StringField('phone number', validators=[
                           DataRequired()])

    day = SelectField('choose date', choices=[
                      ('friday', 'friday 18 dec'), ('sunday', 'sunday 20 dec'), ('friday and sunday', 'friday & sunday 18 & 20 dec')], validators=[DataRequired()])

    seat_no = IntegerField('Seat Number(1 to 300)', validators=[
                           DataRequired()])

    submit = SubmitField('submit')

    def validate_phone_no(self, phone_no):
        no = Records.query.filter_by(phone=phone_no.data).first()
        if no:
            raise ValidationError('Number already exist')
        if phone_no.data.startswith('+') and len(phone_no.data) > 14 or len(phone_no.data) < 11:
            raise ValidationError('invalid phone number')

        if len(phone_no.data) < 11 or len(phone_no.data) > 11:
            raise ValidationError('invalid phone number')

    def validate_seat_no(self, seat_no):

        if seat_no.data > 300 or seat_no.data < 1:
            raise ValidationError(
                'seat number out of range choose from (1 to 300 )')
