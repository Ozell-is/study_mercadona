import base64
import json

from flask import Blueprint, render_template, request, redirect, url_for,flash
from werkzeug.utils import secure_filename

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
def get_admin_page():  # put application's code here
    products = Product.query.all()
    categories = Category.query.all()
    return render_template('admin_page.html', products=products, categories=categories)


@product_ws.get('/admin/create/')
def create_page():

    category = Category.query.all()
    return render_template('create.html', category=category)


@product_ws.post("/admin/create")
def create_product():
    if 'image' in request.files:
        upload_image = request.files['image']

        if upload_image:
            image_data = base64.b64encode(upload_image.read()).decode()

            product_data = {
                "id_product": None,
                "libelle": request.form.get('libelle'),
                "image": image_data,
                "description": request.form.get('description'),
                "price": float(request.form.get('price')),
                "category_id": int(request.form.get('category_id')),
                "pourcentage_promotion": request.form.get('pourcentage_promotion',""),
                "date_debut_promotion": request.form.get('date_debut_promotion',None),
                "date_fin_promotion": request.form.get('date_fin_promotion',None),
            }
            new_product = Product.from_json(product_data)
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for('productWs.get_admin_page'))
    return json.dumps({'success': False}), 400, {'content_type': 'application/json'}


@product_ws.get('/<int:product_id>/edit/')
def edit_page(product_id):
    product = Product.query.get_or_404(product_id)
    category = Category.query.all()
    return render_template('edit.html', product=product, category=category)


@product_ws.post('/<int:product_id>/edit/')
def edit(product_id):
    product = Product.query.get_or_404(product_id)

    image_data = None

    if 'image' in request.files:
        upload_image = request.files['image']

        if upload_image:
            image_data = base64.b64encode(upload_image.read()).decode()
            product.image = image_data

    product.libelle = request.form.get('libelle')
    product.description = request.form.get('description')
    product.price = float(request.form.get('price'))
    product.category_id = int(request.form.get('category_id'))
    product.pourcentage_promotion = int(request.form.get('pourcentage_promotion',None))
    product.date_fin_promotion = request.form.get('date_fin_promotion',None)
    product.date_debut_promotion = request.form.get('date_debut_promotion',None)
    product.image = image_data if image_data is not None else product.image
    db.session.commit()
    return redirect(url_for('productWs.get_admin_page'))

'''

    product.libelle = libelle,
    product.description = description,
    product.date_fin_promotion = date_fin_promotion,
    product.date_debut_promotion = date_debut_promotion,
    product.pourcentage_promotion = pourcentage_promotion,
    product.price = price,
    product.category_id = category_id,
    product.image = image_data
'''



@product_ws.post('/<int:product_id>/delete/')
def delete(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('productWs.get_admin_page'))
