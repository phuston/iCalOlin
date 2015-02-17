from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class loginForm(Form):
    username = StringField(u'What is your username?')
    password = PasswordField(u'What is your password?')
    email = StringField(u'What is your preferred email?')
    submit = SubmitField(u'Submit')