from flask import Blueprint, render_template, request, flash
from ..database.dbconnect import add_user, exist_user
from ..scripts.decorators import login_required

# purpose: page for register new accounts
register = Blueprint("register", __name__)

@register.route("/register", methods=["GET", "POST"])
@login_required
def registrierung_func():
    if request.method == "POST":
        # get user input
        username = request.form["username"]
        password = request.form["password"]
        repeat_password = request.form["repeat_password"]
        # check user input
        correct_input = True
        # check if fields are empty
        if not username:
            flash("username","error")
            correct_input = False
        if not password:
            flash("password","error")
            correct_input = False
        if not repeat_password:
            flash("repeat_password","error")
            correct_input = False
        # check if passwords are equal
        if password != repeat_password and password and repeat_password:
            flash("unequal","error")
            correct_input = False
        # check if username already exists
        if exist_user(username):
            flash("exists","error")
            correct_input = False
        # if user input is correct submit data and create a new account
        if correct_input:
            add_user(username, password)
            flash("success_message","success")
        return render_template("register.html", username=username)
    return render_template("register.html")