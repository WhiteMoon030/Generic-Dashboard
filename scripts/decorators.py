from functools import wraps
from flask import session, redirect, url_for

def login_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if "id" not in session:
            return redirect(url_for("login.login_func"))
        return function(*args, **kwargs)
    return decorated_function