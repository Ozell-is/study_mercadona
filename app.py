from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from bdd.database import db
from config.config import Config

from controller.Adminws import admin_ws
from controller.Productws import product_ws
from controller.Categoryws import category_ws

app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = 't55(4y5y45y45-tg4z'

app.register_blueprint(admin_ws)
app.register_blueprint(product_ws)
app.register_blueprint(category_ws)


db.init_app(app)
with app.app_context():
    db.create_all()


if __name__ == "__main__":

    app.run()
