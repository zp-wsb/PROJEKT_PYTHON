import pytest
from flask import Flask
from main import app  # Importuj aplikację Flask z pliku main.py

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Testuje endpoint '/'"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.data == b'Hello, World!'
