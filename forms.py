#
# Data input form
# forms.py
#

from wtforms import TextField
from wtforms.fields import SubmitField
from wtforms.validators import DataRequired
from flask.ext.wtf import Form

class SymbolSearch(Form):
    minutes = TextField('<b>Minutes</b> (0-59)',
                        validators=[DataRequired()])
    hours   = TextField('<b>Hours 1</b> (0-23)',
                        validators=[DataRequired()])
    day     = TextField('<b>Day 2</b> (0-6)',
                        validators=[DataRequired()])
    submit = SubmitField()
