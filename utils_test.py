import pytest

from utils import *


def test_get_all_posts():
    assert type(get_post_all()) == list


def test_get_posts_by_user():
    assert type(get_posts_by_user('leo')) == list
    assert get_posts_by_user('asdasdfasdf') == []
    assert get_posts_by_user(1) == []


def test_get_comments_by_post_id():
    assert type(get_comments_by_post_id(1)) == list
    assert get_comments_by_post_id(2134234) == []
    assert get_comments_by_post_id('asdasdfasdf') == []
    assert len(get_comments_by_post_id(1)) == 4


def test_search_for_posts():
    assert type(search_for_posts('Утром')) == list


def test_search_for_posts_attribute_error():
    with pytest.raises(AttributeError):
        search_for_posts(1)


def test_get_post_by_pk():
    assert type(get_post_by_pk(1)) == list
    assert get_post_by_pk(2134234) == []
    assert get_post_by_pk('asdasdfasdf') == []
    assert len(get_post_by_pk(1)[0]) == 7
