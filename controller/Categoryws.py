import json

from datetime import date
from flask import Blueprint, current_app, jsonify, render_template, request
from sqlalchemy import func, or_

from bdd.database import db
from models.Category import Category
from models.Product import Product
from controller.catalog import filtered_product

category_ws = Blueprint("categoryWs", __name__, template_folder="templates")





@category_ws.post('/filter_by_category')
def filter_by_category():
    selected_category_libelle = request.json['category_libelle']
    # print(selected_category_libelle)
    new_catalog=filtered_product(selected_category_libelle)

    products = render_template("component/catalog_update.html", products=new_catalog, category=selected_category_libelle, date=date)
    return jsonify({'products': products})

