from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField('Book Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    genre = StringField('Book Genre', validators=[DataRequired()])
    submit = SubmitField('Add Book')


class RemoveBook(FlaskForm):
    id = StringField('Book to remove(ID):', validators=[DataRequired()])
    remove = SubmitField('Remove Book')
