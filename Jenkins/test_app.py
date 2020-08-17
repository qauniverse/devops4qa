import os
import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_one(client):

    rv = client.get('/')
    assert rv.status_code == 200

def test_two(client):
    rv = client.get('/info')
    assert rv.status_code == 200

def test_three(client):
    rv = client.get('/blabla')
    assert rv.status_code == 404