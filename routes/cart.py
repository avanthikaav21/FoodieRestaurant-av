from flask import Blueprint, render_template, redirect, url_for, flash, session, request

from extensions import db
from models.food import Food
from models.cart import Cart
from flask_login import login_required, current_user

cart = Blueprint("cart", __name__)


# =========================
# ADD TO CART
# =========================

@cart.route("/add-to-cart/<int:food_id>")
@login_required
def add_to_cart(food_id):

    food = Food.query.get_or_404(food_id)

    cart_item = Cart.query.filter_by(
        user_id=current_user.id,
        food_id=food.id
    ).first()

    if cart_item:

        cart_item.quantity += 1

    else:

        cart_item = Cart(
            user_id=current_user.id,
            food_id=food.id,
            quantity=1
        )

        db.session.add(cart_item)

    db.session.commit()

    flash("Item added to cart", "success")

    return redirect(url_for("cart.view_cart"))


# =========================
# VIEW CART
# =========================

@cart.route("/cart")
@login_required
def view_cart():

    items = Cart.query.filter_by(
        user_id=current_user.id
    ).all()

    total = sum(
        item.food.price * item.quantity
        for item in items
    )

    return render_template(
        "cart.html",
        items=items,
        total=total
    )


# =========================
# REMOVE ITEM
# =========================

@cart.route("/remove/<int:cart_id>")
@login_required
def remove_item(cart_id):

    item = Cart.query.get_or_404(cart_id)

    db.session.delete(item)
    db.session.commit()

    flash("Item removed", "warning")

    return redirect(url_for("cart.view_cart"))


# =========================
# UPDATE QUANTITY
# =========================

@cart.route("/update/<int:cart_id>/<action>")
@login_required
def update_quantity(cart_id, action):

    item = Cart.query.get_or_404(cart_id)

    if action == "increase":

        item.quantity += 1

    elif action == "decrease" and item.quantity > 1:

        item.quantity -= 1

    db.session.commit()

    return redirect(url_for("cart.view_cart"))