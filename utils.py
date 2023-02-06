import json
#Покрыть тестами все функции


def get_post_all():
    with open('data/posts.json') as f:
        data = json.load(f)
    return data


def get_posts_by_user(user_name):
    data = get_post_all()
    post_by_user = []
    for value in data:
        if value["poster_name"] == user_name:
            post_by_user.append(value)
    return post_by_user


def get_comments_by_post_id(post_id):
    with open('data/comments.json') as f:
        data = json.load(f)
    comments_by_post_id = []
    for value in data:
        if value["post_id"] == post_id:
            comments_by_post_id.append(value)
    return comments_by_post_id


def search_for_posts(query):
    data = get_post_all()
    posts_by_key = []
    for value in data:
        content = value["content"].replace(',', '')
        content = content.replace('.', '')
        if query.lower() in content.lower().split(' '):
            posts_by_key.append(value)
    return posts_by_key


def get_post_by_pk(pk):
    data = get_post_all()
    post_by_pk = []
    for value in data:
        if value['pk'] == pk:
            post_by_pk.append(value)
    return post_by_pk
