from models import User, Role
from extensions import db
from flask_bcrypt import Bcrypt
from extensions import bcrypt


def seed_admin():
    admin = User.query.filter_by(
        username="admin"
    ).first()

    if admin:
        return

    admin_role = Role.query.filter_by(
        role_name="Administrator"
    ).first()

    hashed_password = bcrypt.generate_password_hash(
        "CyberShield123!"
    ).decode("utf-8")

    admin = User(
        username="admin",
        email="admin@cybershield.local",
        password_hash=hashed_password,
        role_id=admin_role.role_id
    )

    db.session.add(admin)
    db.session.commit()