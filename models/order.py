from datetime import datetime

from extensions import db


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    total_amount = db.Column(
        db.Float,
        nullable=False,
        default=0
    )

    delivery_address = db.Column(
        db.Text,
        nullable=False
    )

    payment_method = db.Column(
        db.String(50),
        default="Cash on Delivery"
    )

    payment_status = db.Column(
        db.String(30),
        default="Pending"
    )

    order_status = db.Column(
        db.String(30),
        default="Placed"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    items = db.relationship(
        "OrderItem",
        backref="order",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Order #{self.id}>"



class OrderItem(db.Model):
    __tablename__ = "order_items"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    order_id = db.Column(
        db.Integer,
        db.ForeignKey("orders.id"),
        nullable=False
    )

    food_id = db.Column(
        db.Integer,
        db.ForeignKey("foods.id"),
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        default=1,
        nullable=False
    )

    price = db.Column(
        db.Float,
        nullable=False
    )

    def __repr__(self):
        return (
            f"<OrderItem "
            f"Order:{self.order_id} "
            f"Food:{self.food_id}>"
        )