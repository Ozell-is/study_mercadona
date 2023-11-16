from datetime import timedelta

from flask import Flask, render_template, request
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from bdd.database import db
from config.config import Config
from controller.Adminws import admin_ws
from controller.Categoryws import category_ws
from controller.Loginws import login_ws
from controller.Logoutws import logout_ws
from controller.Productws import product_ws



app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = "t55(4y5y45y45-tg4z"

app.register_blueprint(admin_ws)
app.register_blueprint(product_ws)
app.register_blueprint(category_ws)
app.register_blueprint(login_ws)
app.register_blueprint(logout_ws)

# configuration token JWT
app.config["JWT_SECRET_KEY"] = "hre5h4rz54teaz564"
# Empeche les modification exterieur
app.config["JWT_COOKIE_CSRF_PROTECT"] = True
app.config["JWT_ACCESS_COOKIE_PATH"] = "/api"
app.config["JWT_REFRESH_COOKIE_PATH"] = "/api/tokenRefresh"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()



if __name__ == "__main__":
    create_app().run
