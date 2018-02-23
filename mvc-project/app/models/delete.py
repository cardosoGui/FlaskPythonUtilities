from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators
from wtforms.validators import DataRequired


#Delete - Classe 'DeleteForm' responsavel por validar os dados inputados no formulario deletar o registro no Banco de Dados.

class DeleteForm(Form):
    username = StringField('username', validators=[DataRequired()])