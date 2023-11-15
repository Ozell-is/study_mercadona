import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING']= True
    app.config['SERVER_NAME'] = '127.0.0.1:5000'
    app.config['PREFERED_URL_SCHEME'] = 'http'
    app.config['APPLICATION_ROOT'] ='/'

    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client