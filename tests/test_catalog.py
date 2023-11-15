import app
from controller.catalog import filtered_product, get_category_id_by_libelle
from tests.conftest import app


# test si la catégorie existe
def test_get_category_id_by_libelle(client):
    category_libelle = "viandes"
    category_id = get_category_id_by_libelle(category_libelle)
    assert category_id is not None


# verifie que le filtre renvoi bien une liste de produits
def test_filtered_product(client):
    selected_category_libelle = "viandes"
    filtered_products = filtered_product(selected_category_libelle)

    assert filtered_products is not None
    assert len(filtered_products) > 0
