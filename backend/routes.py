from flask import Blueprint

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return "<h1>Welcome to CyberShield V1</h1>"