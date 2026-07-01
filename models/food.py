from datetime import datetime

from extensions import db


class Food(db.Model):
    __tablename__ = "foods"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    restaurant_id = db.Column(
        db.Integer,
        db.ForeignKey("restaurants.id"),
        nullable=False
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=False
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    image = db.Column(
        db.String(255),
        default="food.jpg"
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    discount_price = db.Column(
        db.Float,
        nullable=True
    )

    stock = db.Column(
        db.Integer,
        default=0
    )

    is_available = db.Column(
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
        backref="food",
        lazy=True,
        cascade="all, delete-orphan"
    )

    order_items = db.relationship(
    "OrderItem",
    backref="food",
    lazy=True,
    cascade="all, delete-orphan"
)
    

    @property
    def final_price(self):
        if self.discount_price and self.discount_price > 0:
            return self.discount_price
        return self.price

    def __repr__(self):
        return f"<Food {self.name}>"