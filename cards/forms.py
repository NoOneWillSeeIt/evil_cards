from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CardForm(FlaskForm):
    is_red = BooleanField()
    card_text = TextAreaField('Текст карточки', validators=[DataRequired()])
    submit = SubmitField('Отправить')
