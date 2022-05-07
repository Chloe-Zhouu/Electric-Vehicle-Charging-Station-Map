from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LocationForm(FlaskForm):
    start_location = StringField('Choose start location', validators=[DataRequired()])
    end_location = StringField('Choose end location', validators=[DataRequired()])
    submit = SubmitField('Search')