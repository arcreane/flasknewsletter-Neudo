from flask import render_template, url_for
from flask_login import login_required, login_user
from sqlalchemy.sql.functions import user
from werkzeug.utils import redirect

from OurApp import app, csrf, bcrypt
from OurApp.forms import LoginForm
from OurApp.models import Users, Categories


@app.route("/")
def hello():
    return render_template("home.html", title="Home", info="Ma page d'accueil dynamique")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/webstart", methods=['POST', 'GET'])
@csrf.exempt
def webstart():
    form = LoginForm()
    print(form.validate_on_submit())
    print(form.login_name.data)
    print(form.errors)
    user = Users.query.filter_by(email=form.login_name.data).first()
    categories = Categories.query.all()
    if form.login_name.data is not None:
        if user.is_admin == 1 and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("newsLetter"))
        else:
            return render_template("webstart.html", title="Webstart", info="Page de presentation de Webstart",
                                   form=form)

    else:
        return render_template("webstart.html", title="Webstart", info="Page de presentation de Webstart", form=form)


@app.route("/login", methods=['POST', 'GET'])
def login():
    # user = Users.query.All.filter_by(email=form.pseudo.data).first()
    return render_template("login.html")


@app.route("/newsLetter")
@login_required
def newsLetter():
    # user = Users.query.All.filter_by(email=form.pseudo.data).first()
    return render_template("login.html")

@app.route("/usersList")
@login_required
def usersList():
    users = Users.query.all()
    return render_template("usersList.html", title="usersList", info="Page de la liste des utilisateurs", users=users)

@app.route("/categoriesList")
@login_required
def categoriesList():
    categories = Categories.query.all()
    return render_template("categoriesList.html", title="categoriesList", info="Page de la liste des categories", categories=categories)
