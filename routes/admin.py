from flask import Blueprint, render_template, redirect, url_for, flash, request

from flask_login import login_required, current_user

from extensions import db

from models.restaurant import Restaurant
from models.food import Food
from models.order import Order


admin = Blueprint("admin", __name__)

@admin.route("/update-order/<int:order_id>/<status>")
def update_order(order_id, status):

    order = Order.query.get_or_404(order_id)

    order.status = status

    db.session.commit()

    flash("Order updated", "success")

    return redirect(url_for("admin.dashboard"))

# =========================
# SIMPLE ADMIN CHECK
# =========================

def admin_required(func):

    def wrapper(*args, **kwargs):

        if not current_user.is_authenticated:

            return redirect(url_for("auth.login"))

        if not getattr(current_user, "is_admin", False):

            flash("Access denied", "danger")

            return redirect(url_for("main.home"))

        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__

    return wrapper


# =========================
# DASHBOARD
# =========================

@admin.route("/dashboard")
@admin_required
def dashboard():

    total_restaurants = Restaurant.query.count()

    total_foods = Food.query.count()

    total_orders = Order.query.count()

    return render_template(
        "admin/dashboard.html",
        total_restaurants=total_restaurants,
        total_foods=total_foods,
        total_orders=total_orders
    )
@admin.route("/add-restaurant", methods=["GET", "POST"])
@admin_required
def add_restaurant():

    if request.method == "POST":

        name = request.form.get("name")

        description = request.form.get("description")

        image_url = request.form.get("image_url")

        restaurant = Restaurant(
            name=name,
            description=description,
            image_url=image_url
        )

        db.session.add(restaurant)
        db.session.commit()

        flash("Restaurant added", "success")

        return redirect(url_for("admin.dashboard"))

    return render_template("admin/add_restaurant.html")
from flask import Blueprint, render_template, request, redirect, url_for, flash

from extensions import db
from models.restaurant import Restaurant
from models.food import Food

admin = Blueprint("admin", __name__)


# Dashboard already here
@admin.route("/dashboard")
def dashboard():
    return "Admin Dashboard"


# ✅ ADD RESTAURANT (if you have)
# @admin.route("/add-restaurant")


# ✅ ADD FOOD (THIS ONE YOU ASKED)
@admin.route("/add-food", methods=["GET", "POST"])
def add_food():

    restaurants = Restaurant.query.all()

    if request.method == "POST":

        food = Food(

            name=request.form.get("name"),

            price=request.form.get("price"),

            restaurant_id=request.form.get("restaurant_id")

        )

        db.session.add(food)
        db.session.commit()

        flash("Food added", "success")

        return redirect(url_for("admin.dashboard"))

    return render_template(
        "admin/add_food.html",
        restaurants=restaurants
    )