from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class LocationForm(FlaskForm):
    start_location = StringField('Choose start city', validators=[DataRequired()])
    end_location = StringField('Choose end city', validators=[DataRequired()])
    submit = SubmitField('Search')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')