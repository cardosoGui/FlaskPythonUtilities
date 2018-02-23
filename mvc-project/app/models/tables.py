from app import db
#Modelando o Banco de dados
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)
    
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        
    def __repr__(self):
        return "%r" % self.username
    
#Produtos
class Product(db.Model):
    __tablename__= "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    price = db.Column(db.Integer)
    buy_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', foreign_keys=buy_id)
    
    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Product %r>" % self.id
#Venda
class Shel(db.Model):
    __tablename__='shel'
    
    id = db.Column(db.Integer, primary_key=True)
    buy_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    user = db.relationship('User',foreign_keys=buy_id)