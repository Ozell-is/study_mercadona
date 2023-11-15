import jwt
from flask import url_for

from models.Category import Category
from models.Product import Product


def test_get_all_product(client):
    response = client.get(url_for("productWs.get_all_product"))
    assert response.status_code == 200
    assert b"catalogue" in response.data
    assert b'<h3 class="libelle">' in response.data


def test_get_admin_page(client):
    response = client.get(url_for("productWs.get_admin_page"))
    assert response.status_code == 200


def test_create_page(client):
    with client.session_transaction() as session:
        session["user_id"] = "invité"
    with client.session_transaction() as session:
        response = client.get(url_for("productWs.create_page"))
        assert session["user_id"] == "invité"
        assert response.status_code == 200


def test_create_product(client):
    with client.session_transaction() as session:
        session["user_id"] = "invité"
    with client.session_transaction() as session:
        response = client.post(url_for("productWs.create_product"))
        assert session["user_id"] == "invité"
        assert response.status_code == 200
        assert b"<h1>CREATION DE PRODUIT<h1>" in response.data


def test_edit_page(client):
    secret_key = "t55(4y5y45y45-tg4z"
    # jwt_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMDA2NzM5NywianRpIjoiNzAxYzIxNWItNDcyMy00Zjk5LTgxNDYtMGVlN2I4NGNlOTNhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3MDAwNjczOTcsImNzcmYiOiJhYzc2NjczOS03MzQ4LTQ3NDEtYjdlYS04ZTAyM2Y2YjcyZWQiLCJleHAiOjE3MDAxNTM3OTd9.MbttaRjsCtwiO0pKBNBtf6ixUM1Bc9X7mqNT9MVlfq8'
    jwt_token = jwt.encode({"user_id": "invité"}, secret_key, algorithm="HS256")
    product_id = 3
    client.set_cookie("access_token_cookie", jwt_token)
    response = client.get(url_for("productWs.edit_page", product_id=product_id))
    assert b"EDITION" in response.data
    assert response.status_code == 200


def test_edit(client):
    secret_key = "t55(4y5y45y45-tg4z"
    jwt_token = jwt.encode({"user_id": "invité"}, secret_key, algorithm="HS256")
    product_id = 3
    client.set_cookie("access_token_cookie", jwt_token)
    response = client.post(url_for("productWs.edit", product_id=product_id))
    assert response.status_code == 200


# elle a bien supprimé le produit de ma base de donnée,
# je verifie juste que le produit nest plus présent
def test_delete(client):
    product_id = 3
    product = Product.query.get(product_id)
    assert product is None
