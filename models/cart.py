from datetime import datetime

from extensions import db


class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    food_id = db.Column(
        db.Integer,
        db.ForeignKey("foods.id"),
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        nullable=False,
        default=1
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    @property
    def unit_price(self):
        return self.food.final_price

    @property
    def total_price(self):
        return self.quantity * self.food.final_price

    def __repr__(self):
        return (
            f"<Cart User:{self.user_id} "
            f"Food:{self.food_id} "
            f"Qty:{self.quantity}>"
        )