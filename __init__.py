from flask import Flask
from .views.register import register
from .views.login import login
from .views.main import main

app = Flask(__name__)
app.secret_key = "fh812ncu2jdnci29ijfmlaKNS"

# register blueprints
app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(main)
