from flask import Blueprint, render_template, request, redirect, url_for

from extensions import bcrypt
from models import User
from flask_login import login_user, logout_user, login_required


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(
            user.password_hash,
            password
        ):
            login_user(user)
            return redirect(url_for("main.dashboard"))

        return "Invalid username or password."

    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))
