
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, TextAreaField
from wtforms.validators import DataRequired, Email
import re


class LocationForm(FlaskForm):
    location = StringField('Location (e.g. Santa Barbara, CA)', validators=[DataRequired()])
    submit = SubmitField('Get Data')
    result, exresult, closest = None, None, None
