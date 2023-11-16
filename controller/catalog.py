from flask import current_app

from models.Category import Category
from models.Product import Product

# recupere l'id de la categorie en fonction du libelle donnée
def get_category_id_by_libelle(libelles):
    with current_app.app_context():
        try:
            category = Category.query.filter_by(_libelle=libelles).first()

            if category:
                return category.id_category
            else:
                print(f"Categorie non trouvée pour le libelle : {libelle}")
                return None
        except Exception as e:
            print(f"Erreur lors de la récupération de l'ID de la catégorie : {str(e)}")
            return None


# recupere les produits en fonction de l'id de la categorie récupérée avec la fonction precedente.
def filtered_product(selected_category_libelle):

    if selected_category_libelle == "all":
        all_product = Product.query.all()
        return all_product
    else:
        category_id = get_category_id_by_libelle(selected_category_libelle)

        if category_id:

            filtered_products = Product.query.filter_by(_category_id=category_id).all()
            converted_products_list = []
            for product in filtered_products:
                converted_products_list.append(
                    {
                        "id_product": product._id_product,
                        "libelle": product.libelle,
                        "description": product.description,

                        "image": product.image,
                        "price": product.price,
                        "date_debut_promotion": product.date_debut_promotion,
                        "date_fin_promotion": product.date_fin_promotion,
                        "pourcentage_promotion": product.pourcentage_promotion,

                    }
                )
            return converted_products_list
