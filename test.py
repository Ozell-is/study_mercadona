from app import db
from models.Product import Product

produit = Product(
    id_product=None,
    libelle="Exemple de produit",
    description="Ceci est un produit factice pour tester",
    price=19.99,
    image=None,  # Vous pouvez ajouter des données d'image si nécessaire
    category_id=None,
    date_debut_promotion="2023-01-01",
    date_fin_promotion="2023-01-15",
    pourcentage_promotion=10.0,
)

try:
    db.session.add(produit)
    db.session.commit()
    print("ok")
except Exception as e:
    print(f"Une erreur s'est produite : {str(e)}")
