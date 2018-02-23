from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

#Update - Classe 'UpdateForm' responsavel por validar os dados inputados no formulario, efetuando a atualizaçao do registro no Banco de Dados.

class UpdateForm(Form):
    username = StringField('username', validators=[DataRequired()])
    name = StringField('name', [validators.Length(max=255)])
    email = EmailField('email', [validators.Email()])