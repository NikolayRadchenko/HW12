import logging

from flask import Blueprint, render_template, request
from functions import search_post

loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route('/list')
def load_photo():
    logging.info("Поиск по постам выполнен")
    tag = request.args.get("tag")
    posts = search_post(tag)
    return render_template('post_list.html', tag=tag, posts=posts)
