from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..database.dbconnect import login_successfull

login = Blueprint("login", __name__)

@login.route("/login", methods=["GET", "POST"])
def login_func():
    if request.method == "POST":
        # get user input
        username = request.form["username"]
        password = request.form["password"]
        # check user input
        check_login = login_successfull(username, password)
        if check_login != 0:
            # create user session
            session["id"] = check_login
            session["username"] = username
            # redirect to main page
            return redirect(url_for("main.main_func"))
        flash("error")
        return render_template("login.html", username=username)
    return render_template("login.html")

@login.route("/logout")
def logout_func():
    session.clear()
    return redirect(url_for("login.login_func"))