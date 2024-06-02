import os
import sys
import pytest
from flask import Flask

# Dodaj katalog nadrzędny do ścieżki wyszukiwania modułów
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
