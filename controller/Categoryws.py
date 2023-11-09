import json

from flask import Blueprint, render_template, request

from bdd.database import db
from models.Category import Category

category_ws = Blueprint("categoryWs", __name__, template_folder="templates")


@category_ws.get("/")
def get_all_category():
    categories = Category.query.all()
    return render_template('', categories=categories)


@category_ws.get("/category")
def get_al_category():  # put application's code here
    data: list[Category] = db.session.query(Category).all()
    return json.dumps(data, default=Category.to_json)


@category_ws.get("/category/<id_category>")
def get_category_by_id(id_category: int):
    data: Category = Category.query.get(id_category)
    return json.dumps(data, default=Category.to_json)


@category_ws.post("/category")
def create_category():
    content_type = request.headers.get("Content-type")
    if content_type == "application/json":
        data: Category = Category.from_json(request.get_json())
        db.session.add(data)
        db.session.commit()
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False}), 400, {"ContentType": "application/json"}


@category_ws.put("/category/<id_category>")
def modify_category(id_category):
    content_type = request.headers.get("Content-type")
    if content_type == "application/json":
        data: Category = Category.from_json(request.get_json())
        data_old = Category.query.get(id_category)
        if data_old is not None:
            data_old_.libelle = data.libelle

        # envoi vers la bdd
        db.session.commit()
        return json.dumps({"success": True}), 200, {"ContentType": "application/json"}
    return json.dumps({"success": False}), 400, {"ContentType": "application/json"}


@category_ws.delete("/category/<id_category>")
def remove_category(id_category: int):
    data = Category.query.get(id_category)
    if type(data) is not None:
        db.session.delete(data)
        db.session.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    return json.dumps({'success': False}), 200, {'ContentType': 'application/json'}
