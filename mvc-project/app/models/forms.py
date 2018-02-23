from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

#Login - Classe 'LoginFomr' responsavel por validar os dados inputados no efetuar o login, disponibilizando algumas features para o usuario logado.. atraves do registro no Banco de Dados.
class LoginForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    remember_me = BooleanField('remember_me')