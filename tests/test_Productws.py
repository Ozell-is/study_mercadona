from flask import url_for

def test_get_all_product(client):
    response = client.get(url_for('productWs.get_all_product'))
    assert b'catalogue' in response.data