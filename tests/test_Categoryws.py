from flask import url_for


def test_filter_by_category(client):
    data = {"category_libelle": "viandes"}
    response = client.post(
        "/filter_by_category", json=data, headers={"Content-Type": "application/json"}
    )

    assert response.status_code == 200
