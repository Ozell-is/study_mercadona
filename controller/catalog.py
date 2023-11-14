from flask import current_app

from models.Category import Category
from models.Product import Product

def get_category_id_by_libelle(libelles):
    with current_app.app_context():
        try:
            category = Category.query.filter_by(_libelle=libelles).first()
            print(category)
            if category:
                print(category.id_category)
                return category.id_category
            else:
                print(f"Categorie non trouvée pour le libelle : {libelle}")
                return None
        except Exception as e:
            print(f"Erreur lors de la récupération de l'ID de la catégorie : {str(e)}")
            return None


def filtered_product(selected_category_libelle):
    # Vérifiez si la catégorie sélectionnée est 'all'
    if selected_category_libelle == 'all':
        all_product = Product.query.all()
        return all_product
    else:
        category_id = get_category_id_by_libelle(selected_category_libelle)
        print(category_id)

        # Vérifiez si la catégorie a été trouvée
        if category_id:
            # Utilisez l'ID de la catégorie pour filtrer les produits
            filtered_products = Product.query.filter_by(_category_id=category_id).all()
            converted_products_list = []
            for product in filtered_products:
                converted_products_list.append({
                    "id_product": product._id_product,
                    "libelle": product.libelle,
                    "description": product.description,
                    #"category_name": product.category.libelle,
                    "image": product.image,
                    "price": product.price,
                    "date_debut_promotion": product.date_debut_promotion,
                    "date_fin_promotion": product.date_fin_promotion,
                    "pourcentage_promotion": product.pourcentage_promotion,
                    # "new_price": product.price * (1 - (product._pourcentage_promotion / 100))
                })
            return converted_products_list
