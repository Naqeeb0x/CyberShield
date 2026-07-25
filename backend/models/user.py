from flask_login import UserMixin
from extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    user_id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.role_id"),
        nullable=False
    )

    def get_id(self):
        return str(self.user_id)

    def __repr__(self):
        return f"<User {self.username}>"