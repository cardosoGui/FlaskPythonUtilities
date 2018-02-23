from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

#Register - Classe 'RegistrationFrom' responsavel por validar os dados inputados no formulario e inserir os registros no Banco de Dados.
class RegistrationForm(Form):
    username = StringField('username', [validators.DataRequired(), validators.Length(max=50)])
    name = StringField('name', [validators.Length(max=255)])
    email = EmailField('email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    accept_terms = BooleanField('I accept the Terms...', [validators.DataRequired()])
    