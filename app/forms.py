from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class loginForm(Form):
    username = StringField('What is your username?')
    password = PasswordField('What is your password?')
    email = StringField('What is your preferred email?')
    submit = SubmitField('Submit')