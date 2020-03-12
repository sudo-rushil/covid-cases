
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import re

class LocationForm(FlaskForm):
    location = StringField('Location (e.g. Santa Barbara, CA)', validators=[DataRequired()])
    submit = SubmitField('Get Data')
    result, exresult, closest = None, None, None
