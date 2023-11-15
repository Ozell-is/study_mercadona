from flask import url_for


# test sans jwt
def test_redirection(client):
    response = client.get(url_for("loginWs.redirection"))
    assert response.status_code == 302


def test_login_page(client):
    response = client.get(url_for("loginWs.login_page"))
    assert response.status_code == 200
    assert b"connexion"


def test_authenticator(client):
    form_data = {"username": "user", "password": "pass"}
    response = client.post(url_for("loginWs.authenticator", data=form_data))

    assert response.status_code == 302
