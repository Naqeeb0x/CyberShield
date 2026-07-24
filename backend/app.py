from flask import Flask

from config import Config
from extensions import db, bcrypt, login_manager
from models import User, Role
from seeds.seed_roles import seed_roles
from seeds.seed_admin import seed_admin
from routes import main

# Create Flask application
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# Initialize database
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "auth.login"


bcrypt.init_app(app)
app.register_blueprint(main)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_roles()
        seed_admin()

    app.run(debug=Config.DEBUG)

    app.run(debug=Config.DEBUG)