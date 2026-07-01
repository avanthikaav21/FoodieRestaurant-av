from flask import Blueprint, render_template
from flask_login import login_required, current_user
from models.order import Order

order = Blueprint("order", __name__)


@order.route("/my-orders")
@login_required
def my_orders():

    orders = Order.query.filter_by(user_id=current_user.id).all()

    return render_template(
        "my_orders.html",
        orders=orders
    )