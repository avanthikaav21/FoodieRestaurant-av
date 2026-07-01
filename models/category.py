from datetime import datetime

from extensions import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    image = db.Column(
        db.String(255),
        default="category.jpg"
    )

    description = db.Column(
        db.Text,
        nullable=True
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
        backref="category",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Category {self.name}>"