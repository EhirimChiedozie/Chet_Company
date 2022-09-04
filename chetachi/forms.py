from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class OrderForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=4, max=40)])
    current_location = StringField('Current location', validators=[DataRequired(), Length(min=4, max=500)])
    phonenumber1 = StringField('Phonenumber1', validators=[DataRequired(), Length(min=4, max=20)])
    phonenumber2 = StringField('Phonenumber2', validators=[Length(min=4, max=20)])
    description = StringField('Enter a short description of your order', validators=[DataRequired(), Length(min=4, max=500)])
    submit = SubmitField('Submit')