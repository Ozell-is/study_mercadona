from app import db, app

from models.Product import Product
from models.Category import Category





# Créez un contexte d'application
with app.app_context():
    # Tout d'abord, récupérez la catégorie à laquelle vous voulez lier le produit.
    # Vous pouvez utiliser le nom de la catégorie ou son ID, selon ce qui est disponible.
    nouvelle_category = Category (
        id_category=None,
        libelle="surgelées"
    )

    # Ajoutez le nouveau produit à la base de données et committez les changements
    db.session.add(nouvelle_category)
    db.session.commit()

    # Vérifiez que le produit a bien été créé
    print("Nouveau produit créé avec l'ID:", nouvelle_category.id_category)
