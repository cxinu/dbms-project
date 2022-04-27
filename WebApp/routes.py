from flask import render_template, request, redirect, url_for, session, flash
from WebApp import app, db
from WebApp.forms import LoginForm, RegistrationForm, authForm
from WebApp.models import User


@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("verify"))
    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            fname=form.firstName.data,
            username=form.username.data,
            phone=form.phone.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("verify"))
    return render_template("register.html", form=form)


@app.route("/verify", methods=["GET", "POST"])
def verify():
    if "number" in session:
        return redirect(url_for("home"))

    form = authForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template("verify.html", form=form)


@app.route("/home", methods=["GET", "POST"])
def home():
    # if "number" in session:
    #     number = session["number"]
    #     name = session["FirstName"]
    #     username = session["username"]
    #     return render_template("home.html", number=number, name=name, username=username)
    # else:
    #     return redirect(url_for("login"))
    return render_template("home.html")


@app.route("/project", methods=["GET"])
def project():
    return render_template("project.html")


@app.route("/github", methods=["GET"])
def github():
    return render_template("github.html")


@app.route("/logout")
def logout():
    session.pop("number", None)
    return redirect(url_for("login"))
