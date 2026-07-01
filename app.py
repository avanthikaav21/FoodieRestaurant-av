import os
from flask import Flask
from routes.main import main
from config import Config
from extensions import db, bcrypt, login_manager, migrate
from models.user import User

# Import Models
from models.restaurant import Restaurant
from models.category import Category
from models.food import Food
from models.cart import Cart
from models.order import Order
from routes.auth import auth
from routes.restaurant import restaurant
from routes.cart import cart
from routes.order import order
from routes.admin import admin
def create_app():

    app = Flask(__name__)
    app.register_blueprint(main)
    app.config.from_object(Config)

    # create folders
    os.makedirs(
        os.path.join(app.root_path, "instance"),
        exist_ok=True
    )

    os.makedirs(
        app.config["UPLOAD_FOLDER"],
        exist_ok=True
    )

    # init extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # user loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(restaurant, url_prefix="/restaurant")
    app.register_blueprint(cart, url_prefix="/cart")
    app.register_blueprint(order, url_prefix="/order")
    app.register_blueprint(admin, url_prefix="/admin")
    
    

    with app.app_context():
        db.create_all()

    return app


app = create_app()
from routes.admin import admin



if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )