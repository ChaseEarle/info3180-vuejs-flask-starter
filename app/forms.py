from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired(), Length(max=255)])
    description = TextAreaField('Description', validators=[DataRequired()])
    poster = FileField('Movie Poster', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Only JPG, JPEG, or PNG images are allowed.')])
    submit = SubmitField('Submit')
