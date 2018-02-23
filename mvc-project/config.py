#Caminho do Arquivo de Banco de Dados
import os.path
basedir = os.path.abspath(os.path.dirname(__file__))
#Console Debug, direto do navegador
DEBUG = True
#Config de acesso ao Banco de dados
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'storage.db')
#A cada atualizaçao salva nos arquivos, o servidor reinicia de forma automatica "Exceto em Erro de Sintaxe do Python"
SQLALCHEMY_TRACK_MODIFICATIONS = True
#Chave secreta
SECRET_KEY = 'CardosoGui'