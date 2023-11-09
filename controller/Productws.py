import base64
import json

from flask import Blueprint, render_template, request, redirect, url_for
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
    return render_template('create.html')


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
                "pourcentage_promotion": request.form.get('pourcentage_promotion'),
                "date_debut_promotion": datetime.strptime(request.form.get('date_debut_promotion'), '%d-%m').date(),
                "date_fin_promotion": datetime.strptime(request.form.get('date_fin_promotion'), '%d-%m').date(),
            }
            new_product = Product.from_json(product_data)
            db.session.add(new_product)
            db.session.commit()
            return redirect(url_for('productWs.get_admin_page'))
    return json.dumps({'success': False}), 400, {'content_type': 'application/json'}


@product_ws.get('/<int:product_id>/edit/')
def edit_page(product_id):
    product = Product.query.get_or_404(product_id)
    product_edit = Product.to_json(product)
    return render_template('edit.html', product=product_edit)


@product_ws.post('/<int:product_id>/edit/')
def edit(product_id):
    product = Product.query.get_or_404(product_id)


    libelle = request.form['libelle']
    description = request.form['description']
    price = float(request.form['price'])
    category_id = int(request.form['category_id'])
    pourcentage_promotion = request.form['pourcentage_promotion']
    date_fin_promotion = datetime.strptime(request.form['date_fin_promotion'],'%d-%m').date()
    date_debut_promotion = datetime.strptime(request.form['date_debut_promotion'],'%d-%m').date()
    image_data = request.form['image']

    product.libelle = libelle,
    product.description = description,
    product.date_fin_promotion = date_fin_promotion,
    product.date_debut_promotion = date_debut_promotion,
    product.pourcentage_promotion = pourcentage_promotion,
    product.price = price,
    product.category_id = category_id,
    product.image = image_data
    product_edit = Product.from_json(product)
    db.session.add(product_edit)
    db.session.commit()

    return redirect(url_for('productWs.index'))



@product_ws.post('/<int:product_id>/delete/')
def delete(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('productWs.get_admin_page'))
