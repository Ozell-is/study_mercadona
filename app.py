# -*- coding: utf-8 -*-


from flask import Flask, render_template

from bdd.database import db
from config.config import Config
from controller.Adminws import admin_ws
from controller.Productws import product_ws

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(admin_ws)
app.register_blueprint(product_ws)


db.init_app(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()


@app.route("/admin")
def login():
    return render_template("admin_page.html")
