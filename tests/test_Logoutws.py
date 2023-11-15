import requests
from flask import url_for


def test_logout(client):
    response = client.post(url_for("logoutWs.logout"))
    assert response == 302

    session = requests.Session()
    assert "access_token_cookie" not in session.cookies
    assert "refresh_token_cookie" not in session.cookies
