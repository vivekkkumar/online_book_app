from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User

# checking if email already exists for validators
def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email Already Exists')

# these are fields or forms that the user fills

# can add any number of validators to a form within a list.
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(3,30, message='between 3 to 20 characters')])
    email = StringField('Email', validators=[DataRequired(), Email(), email_exists])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='password must match')])
    # should be same name for the object which was given above , EqualTo
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('Remember Me')
    submit = SubmitField('LogIn')
