from models import Role
from extensions import db


def seed_roles():
    default_roles = [
        "Administrator",
        "SOC Analyst",
        "Security Manager",
        "Read Only"
    ]

    for role_name in default_roles:
        role = Role.query.filter_by(role_name=role_name).first()

        if role is None:
            db.session.add(Role(role_name=role_name))

    db.session.commit()