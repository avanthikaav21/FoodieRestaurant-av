from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from extensions import db
from models.user import User
from forms.auth_forms import (
    RegisterForm,
    LoginForm
)

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = RegisterForm()

    if form.validate_on_submit():

        email_exists = User.query.filter_by(
            email=form.email.data
        ).first()

        username_exists = User.query.filter_by(
            username=form.username.data
        ).first()

        if email_exists:
            flash(
                "Email already exists.",
                "danger"
            )
            return redirect(url_for("auth.register"))

        if username_exists:
            flash(
                "Username already exists.",
                "danger"
            )
            return redirect(url_for("auth.register"))

        user = User(
            full_name=form.full_name.data,
            username=form.username.data,
            email=form.email.data,
            phone=form.phone.data
        )

        user.set_password(
            form.password.data
        )

        db.session.add(user)
        db.session.commit()

        flash(
            "Registration Successful. Please Login.",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "register.html",
        form=form
    )


@auth.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("main.home"))

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and user.check_password(
            form.password.data
        ):

            login_user(user)

            flash(
                "Welcome Back!",
                "success"
            )

            return redirect(
                url_for("main.home")
            )

        flash(
            "Invalid Email or Password",
            "danger"
        )

    return render_template(
        "login.html",
        form=form
    )


@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Logged out successfully.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )