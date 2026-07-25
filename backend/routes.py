from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("home.html")


@main.route("/dashboard")
@login_required
def dashboard():
    return f"""
    <h1>CyberShield Dashboard</h1>

    <p>Welcome, {current_user.username}!</p>

    <p>You are successfully authenticated.</p>

    <a href="/logout">Logout</a>
    """
