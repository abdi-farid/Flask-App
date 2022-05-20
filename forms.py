"""
    class defining the form
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddTask(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')


class DeleteTAsk(FlaskForm):
    submit = SubmitField('Delete')
