from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, login_manager
#Importando todos os objetos referente a Formulario e validacoes
from app.models.tables import User
from app.models.forms import LoginForm
from app.models.register import RegistrationForm
from app.models.update import UpdateForm
from app.models.delete import DeleteForm

#Cache de conexao generico

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=True)
            return redirect(url_for("index"))
            flash("Logged in")
        else:
            flash("Invalid Login")
    return render_template('login.html',
                          form_login=form)

@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))


@app.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        user = User(form.username.data, form.password.data,
                    form.name.data, form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form_registration=form)

#Esta funçao responsavel por atualidar dados "Nome" e "Email" do usuario solicitando "Login como confirmaçao simples"

@app.route("/update", methods=["GET","POST"])
def update():
    form = UpdateForm(request.form)
    user = User.query.filter_by(username=form.username.data).first()
    if request.method == "POST" and form.validate():
        if user and user.username == form.username.data:
            user.name = form.name.data
            user.email = form.email.data
            db.session.add(user)
            db.session.commit()
            flash('Update Complete')
            return redirect(url_for('index'))
        else:
            flash("Login Required")
            return redirect(url_for('login'))
    return render_template('update.html', form_update=form)

@app.route("/list", methods=["GET","POST"])
def Users():
    users = User.query.order_by(User.username).all()
    form = DeleteForm(request.form)
    select = User.query.filter_by(username=form.username.data).first()
    if users == None:
        flash("Please Create Users")
        return redirect(url_for('index'))
    if request.method == "POST" and form.validate():
        db.session.delete(select)
        db.session.commit()
        flash("Deleted")
        return redirect(url_for('index'))
    return render_template('list_users.html', users_list = users,
                          delete_form = form)