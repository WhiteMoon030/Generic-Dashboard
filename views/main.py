from flask import Blueprint, render_template
from ..scripts.decorators import login_required

main = Blueprint("main", __name__)

@main.route("/")
@login_required
def main_func():
    return render_template("main.html")