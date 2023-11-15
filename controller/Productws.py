import base64
import json
from datetime import date

from flask import (Blueprint, flash, make_response, redirect, render_template,
                   request, url_for)
from flask_jwt_extended import (get_jwt_identity, jwt_required,
                                verify_jwt_in_request)
from werkzeug.utils import secure_filename

from bdd.database import db
from models.Category import Category
from models.Product import Product

product_ws = Blueprint("productWs", __name__, template_folder="templates")


@product_ws.get("/")
def get_all_product():
    products = Product.query.all()
    categories = Category.query.all()
    return render_template(
        "home.html", products=products, categories=categories, date=date
    )


@product_ws.get("/api/admin")
@jwt_required()
def get_admin_page():
    products = Product.query.all()
    categories = Category.query.all()
    return render_template(
        "admin_page.html", products=products, categories=categories, date=date
    )


@product_ws.get("/api/admin/create/")
@jwt_required()
def create_page():
    category = Category.query.all()
    return render_template("create.html", category=category)


@product_ws.post("/api/admin/create")
def create_product():
    if "image" in request.files:
        upload_image = request.files["image"]

        if upload_image:
            image_data = base64.b64encode(upload_image.read()).decode()
            pourcentage_promotion_str = request.form.get("pourcentage_promotion")
            pourcentage_promotion = (
                int(pourcentage_promotion_str)
                if pourcentage_promotion_str.isdigit()
                else None
            )

            product_data = {
                "id_product": None,
                "libelle": request.form.get("libelle"),
                "image": image_data,
                "description": request.form.get("description"),
                "price": float(request.form.get("price")),
                "category_id": int(request.form.get("category_id")),
                "pourcentage_promotion": pourcentage_promotion,
                "date_debut_promotion": request.form.get("date_debut_promotion")
                or None,
                "date_fin_promotion": request.form.get("date_fin_promotion") or None,
            }
            new_product = Product.from_json(product_data)
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for("productWs.get_admin_page"))
    return json.dumps({"success": False}), 400, {"content_type": "application/json"}


@product_ws.get("/api/<int:product_id>/edit/")
@jwt_required()
def edit_page(product_id):
    product = Product.query.get_or_404(product_id)
    category = Category.query.all()
    return render_template("edit.html", product=product, category=category)


@product_ws.post("/api/<int:product_id>/edit/")
def edit(product_id):
    product = Product.query.get_or_404(product_id)

    image_data = None

    if "image" in request.files:
        upload_image = request.files["image"]

        if upload_image:
            image_data = base64.b64encode(upload_image.read()).decode()
            product.image = image_data

    product.libelle = request.form.get("libelle")
    product.description = request.form.get("description")
    product.price = float(request.form.get("price"))
    product.category_id = int(request.form.get("category_id"))
    product.pourcentage_promotion = int(request.form.get("pourcentage_promotion", None))
    product.date_fin_promotion = request.form.get("date_fin_promotion", None)
    product.date_debut_promotion = request.form.get("date_debut_promotion", None)
    product.image = image_data if image_data is not None else product.image
    db.session.commit()
    return redirect(url_for("productWs.get_admin_page"))


@product_ws.post("/api/<int:product_id>/delete/")
def delete(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for("productWs.get_admin_page"))
