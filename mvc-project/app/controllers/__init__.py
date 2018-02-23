from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

#Iniciando o aplicativo e o sistema de Banco de dados

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Iniciando sistema de login ao 'app'

manager = Manager(app)
manager.add_command('db',MigrateCommand)
login_manager = LoginManager(app)
#Importanto o 'Models = Database'
#Importanto o 'Controllers = Logica do sistema'
from app.models import tables, forms
from app.controllers import default