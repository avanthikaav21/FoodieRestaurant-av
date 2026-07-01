from datetime import datetime

from flask_login import UserMixin

from extensions import db, bcrypt


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    full_name = db.Column(
        db.String(120),
        nullable=False
    )

    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    phone = db.Column(
        db.String(20),
        nullable=True
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    profile_image = db.Column(
        db.String(255),
        default="default.png"
    )

    address = db.Column(
        db.Text,
        nullable=True
    )

    is_admin = db.Column(
        db.Boolean,
        default=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Relationships
    cart_items = db.relationship(
        "Cart",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    orders = db.relationship(
        "Order",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # Password Methods
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

    def check_password(self, password):
        return bcrypt.check_password_hash(
            self.password,
            password
        )

    def __repr__(self):
        return f"<User {self.username}>"