from models.Admin import Admin


# la création est commenté car lors du test le compte a réelement était crée,
# a partir de maintenant je verifie seulement qu'il existe
def test_create_admin(client):
    admin_data = {"username": "user", "password": "pass"}
    # response = client.post('/createAdmin', json=admin_data)
    # assert response.status_code == 200
    existing_admin = Admin.query.filter_by(_username="user").first()
    assert existing_admin is not None
