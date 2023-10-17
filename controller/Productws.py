import json

from flask import Blueprint, render_template, request

from bdd.database import db
from models.Product import Product
from models.Category import Category

product_ws = Blueprint("productWs", __name__, template_folder="templates")

@product_ws.get("/")
def get_all_product():
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('home.html', products=products, categories=categories)

@product_ws.get("/admin")
def get_al_product():  # put application's code here
    data: list[Product] = db.session.query(Product).all()
    return json.dumps(data, default=Product.to_json)


@product_ws.get("/product/<id_product>")
def get_product_by_id(id_product: int):
    data: Product = Product.query.get(id_product)
    return json.dumps(data, default=Product.to_json)


@product_ws.post("/product")
def create_product():
    content_type = request.headers.get("Content-type")
    if content_type == "application/json":
        data: Product = Product.from_json(request.get_json())
        db.session.add(data)
        db.session.commit()
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False}), 400, {"ContentType": "application/json"}


@product_ws.put("/product/<id_product>")
def modify_product(id_product):
    content_type = request.headers.get("Content-type")
    if content_type == "application/json":
        data: Product = Product.from_json(request.get_json())
        data_old = Product.query.get(id_product)
        if data_old is not None:
            data_old.libelle = data.libelle
            data_old.description = data.description
            data_old.price = data.price
            data_old.image = data.image
            data_old.category_id = data.category_id
            data_old.date_debut_promotion = data.date_debut_promotion
            data_old.date_fin_promotion = data.date_fin_promotion
            data_old.pourcentage_promotion = data.pourcentage_promotion

        # envoi vers la bdd
        db.session.commit()
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False}), 400, {"ContentType": "application/json"}


@product_ws.delete("/product/<id_product>")
def remove_product(id_product: int):
    data = Product.query.get(id_product)
    if type(data) is not None:
        db.session.delete(data)
        db.session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
