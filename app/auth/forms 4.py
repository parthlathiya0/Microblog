from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from app.models import User  #to store in db, in table 'user' of Class 'User'
from flask_babel import lazy_gettext as _l

class LoginForm(FlaskForm):
    username = StringField(_l('Username', validators=[DataRequired()]))
    password = PasswordField(_l('Password', validators=[DataRequired()]))
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))

class RegistrationForm(FlaskForm):
    username = StringField(_l('Username', validators=[DataRequired()]))
    email = StringField(_l('Email', validators=[DataRequired(), Email()]))
    password = PasswordField(_l('Password', validators=[DataRequired()]))
    password2 = PasswordField(_l(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')]))
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l('Please use a different email address.'))

class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email', validators=[DataRequired(), Email()]))
    submit = SubmitField(_l('Request Password Reset'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password', validators=[DataRequired()]))
    password2 = PasswordField(_l('Repeat Password', validators=[DataRequired(), EqualTo('password')]))
    submit = SubmitField(_l('Request Password Reset'))