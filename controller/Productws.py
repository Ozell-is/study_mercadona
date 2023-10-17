import json

from flask import Blueprint, render_template, request,redirect, url_for
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
    if request.method == 'POST':
        libelle = request.form['libelle']
        description = request.form['description']
        date_debut_promotion = request.form['date_debut_promotion']
        date_fin_promotion = request.form['date_fin_promotion']
        price = float(request.form['price'])
        pourcentage_promotion = int(request.form['pourcentage_promotion'])
        category_id = int(request.form['category_id'])

        image = None
        if 'image' in request.files:
            image = request.files['image']

        if image and image.filename != '':
            # Lisez le fichier binaire de l'image
            image_data = image.read()
        else:
            image_data = None

        produit = Product(libelle=libelle,
                          description=description,
                          date_fin_promotion=date_fin_promotion,
                          date_debut_promotion=date_debut_promotion,
                          pourcentage_promotion=pourcentage_promotion,
                          price=price,
                          category_id=category_id,
                          image=image_data)
        db.session.add(produit)
        db.session.commit()

        return redirect(url_for('productWs.get_admin_page'))

@product_ws.get('/<int:product_id>/edit/')
def edit_page(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('edit.html', product=product)

@product_ws.post('/<int:product_id>/edit/')
def edit(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        libelle = request.form['libelle']
        description = request.form['description']
        date_fin_promotion = request.form['date_fin_promotion']
        price = float(request.form['price'])
        category_id = int(request.form['category_id'])
        pourcentage_promotion = float(request.form['pourcentage_promotion'])
        date_debut_promotion = request.form['date_debut_promotion']

        product.libelle = libelle,
        product.description = description,
        product.date_fin_promotion = date_fin_promotion,
        product.date_debut_promotion = date_debut_promotion,
        product.pourcentage_promotion = pourcentage_promotion,
        product.price = price,
        product.category_id = category_id,
        product.image = image_data

        db.session.add(product)
        db.session.commit()

        return redirect(url_for('productWs.index'))

    return render_template('edit.html', product=product)

@product_ws.post('/<int:product_id>/delete/')
def delete(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('productWs.get_admin_page'))