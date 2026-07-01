from datetime import datetime

from extensions import db


class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False,
        unique=True
    )

    image = db.Column(
        db.String(255),
        default="restaurant.jpg"
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    address = db.Column(
        db.Text,
        nullable=False
    )

    city = db.Column(
        db.String(100),
        nullable=False
    )

    phone = db.Column(
        db.String(20),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        nullable=True
    )

    opening_time = db.Column(
        db.String(20),
        nullable=False
    )

    closing_time = db.Column(
        db.String(20),
        nullable=False
    )

    rating = db.Column(
        db.Float,
        default=5.0
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    # Relationship
    foods = db.relationship(
        "Food",
        backref="restaurant",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Restaurant {self.name}>"