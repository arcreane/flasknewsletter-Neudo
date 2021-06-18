from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class LoginForm(FlaskForm):
    login_name = StringField("Login")
    password = PasswordField("Password")
    submit_button = SubmitField("Submit")
