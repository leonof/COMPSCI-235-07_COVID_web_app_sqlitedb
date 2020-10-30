import pytest

from flask import session



def test_index(client):
    # Check that we can retrieve the home page.
    response = client.get('/')
    assert response.status_code == 200
    assert b'Movie List' in response.data


def test_search(client):
    response = client.post('/?search=2016')
    assert response.status_code == 200
    assert b'2016' in response.data


