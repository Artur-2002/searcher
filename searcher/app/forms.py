from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.widgets import TextArea


class PostForm(FlaskForm):
    text = StringField(u'Text', widget=TextArea())
    submit = SubmitField('Найти')