import unittest
from app import app

def test_flask_greeding():
    with app.test_client() as client:
        response = app.test_client().get('/')
        assert response.status_code == 200
        assert response.data == b'Hello, World!'
