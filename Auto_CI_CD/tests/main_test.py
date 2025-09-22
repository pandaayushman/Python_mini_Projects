import pytest
from app.main import app

def testing():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data == b"Successfully tested the pipeline :) "
        