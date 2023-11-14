import json

from sqlalchemy import func, or_

from app import app, db
from models.Category import Category
from models.Product import Product

with app.app_context():
    category_ids = [category.id_category for category in Category.query.all()]
    print(category_ids)
    print(Category.libelle)

'''
def print_categories():
    try:
        with app.app_context():
            # Récupérez toutes les catégories
            categories = Category.query.all()

            # Affichez les catégories dans la console
            for category in categories:
                print(f"Category ID: {category.id_category}, Libelle: {category.libelle}")

            return json.dumps({'message': 'Categories printed in the console'})
    except Exception as e:
        print(str(e))
        return json.dumps({'error': 'Une erreur s\'est produite lors de l\'impression des catégories.'}), 500

# Exécutez la fonction dans le contexte de l'application Flask
print_categories()
'''
