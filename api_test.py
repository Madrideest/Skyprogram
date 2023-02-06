import pytest

from main import app


def test_app_posts_list():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list
    assert response.status_code == 200


def test_app_posts_key():
    response = app.test_client().get('/api/posts')
    assert "poster_name" in response.json[0]
    assert "poster_avatar" in response.json[0]
    assert "pic" in response.json[0]
    assert "content" in response.json[0]
    assert "views_count" in response.json[0]
    assert "likes_count" in response.json[0]
    assert "pk" in response.json[0]


def test_app_posts_by_id_dict():
    response = app.test_client().get('/api/posts/1')
    assert type(response.json) == dict
    assert response.status_code == 200


def test_app_posts_by_id_key():
    response = app.test_client().get('/api/posts/1')
    assert "poster_name" in response.json
    assert "poster_avatar" in response.json
    assert "pic" in response.json
    assert "content" in response.json
    assert "views_count" in response.json
    assert "likes_count" in response.json
    assert "pk" in response.json
