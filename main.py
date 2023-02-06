from flask import Flask, render_template, request, jsonify
import logging
from utils import *


api_logger = logging.getLogger()

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('api.log')

formatter_console = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
formatter_file = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

console_handler.setFormatter(formatter_console)
file_handler.setFormatter(formatter_file)

api_logger.addHandler(console_handler)
api_logger.addHandler(file_handler)

app = Flask(__name__)


@app.route('/')
def index_page():
    posts = get_post_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def post_page(postid):
    comments = get_comments_by_post_id(postid)
    poster_data = get_post_by_pk(postid)[0]
    count_comments = len(comments)
    return render_template('post.html', poster_data=poster_data, comments=comments, count_comments=count_comments)


@app.route('/search')
def search_page():
    s = request.args.get('s')
    posts_count = 0
    if s:
        posts = search_for_posts(s)
        posts_count = len(posts)
        return render_template('search.html', posts=posts, posts_count=posts_count)
    else:
        return render_template('search.html', posts_count=posts_count)


@app.route('/users/<username>')
def post_by_user_page(username):
    post_by_user = get_posts_by_user(username)
    return render_template('user-feed.html', post_by_user=post_by_user, username=username)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error=error), 404


@app.errorhandler(500)
def not_found_error(error):
    return render_template('500.html', error=error), 500


@app.route('/api/posts', methods=['GET'])
def api_posts():
    api_logger.warning(f'Запрос /api/posts')
    return jsonify(get_post_all())


@app.route('/api/posts/<int:post_id>', methods=['GET'])
def api_post_by_id(post_id):
    api_logger.warning(f'Запрос /api/posts/{post_id}')
    return jsonify(get_post_by_pk(post_id)[0])


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
