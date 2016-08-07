from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(Form):
    email = StringField('E-post', validators=[DataRequired(),
                                            Email(),
                                            Length(1,127)])
    password = PasswordField('Passord', validators=[DataRequired()])
    remember_me = BooleanField('Husk meg')
    submit = SubmitField('Logg inn')