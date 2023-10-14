import json

from flask import Blueprint, render_template, request

from bdd.database import db
from models.Product import Product

product_ws = Blueprint("productWs", __name__, template_folder="templates")

list_product: list = []


@product_ws.get("/")
def get_all_product():  # put application's code here
    return json.dumps(list_product, default=Product.to_json)


@product_ws.get("/admin/<id_product>")
def get_product_by_id(id_product: int):
    data: list[Product] = (
        db.session.query(Product).filter(Product.id_product == id_product).one()
    )
    return json.dumps(data, default=Product.to_json)


@product_ws.post("/admin")
def create_product():
    content_type = request.headers.get("Content-type")
    if content_type == "application/json":
        data: Product = Product.from_json(request.get_json())
        list_product.append(data)
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False}), 400, {"ContentType": "application/json"}


@product_ws.put("/admin")
def modify_product():
    content_type = request.headers.get("Content-type")
    if content_type == "application/json":
        data: Product = json.loads(request.data)

        old_product: Product = (
            db.session.query(Produit)
            .filter(Product.id_product == data.id_product)
            .one()
        )

        old_product.libelle = data.libelle
        old_product.description = data.description
        old_product.price = data.price
        old_product.image = data.image
        old_product.id_category = data.id_category
        db.session.commit()
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False}), 400, {"ContentType": "application/json"}


@product_ws.delete("/admin/<id_product>")
def remove_product(id_product: int):
    data: Product = (
        db.session.query(Product).filter(Product.id_product == id_product).one()
    )
    if type(data) != None:
        db.session.delete(data)
        return (
            json.dumps({"success": True}),
            200,
            {"ContentType": "application/json"},
        )
    return json.dumps({"success": False}), 200, {"ContentType": "application/json"}
