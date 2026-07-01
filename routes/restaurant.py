from flask import Blueprint, render_template
from models.restaurant import Restaurant

restaurant = Blueprint("restaurant", __name__)


@restaurant.route("/restaurants")
def all_restaurants():

    restaurants = Restaurant.query.all()

    return render_template(
        "restaurants.html",
        restaurants=restaurants
    )


@restaurant.route("/restaurant/<int:id>")
def restaurant_detail(id):

    restaurant = Restaurant.query.get_or_404(id)

    return render_template(
        "restaurant_detail.html",
        restaurant=restaurant
    )