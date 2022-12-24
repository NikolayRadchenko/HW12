import json
from json import JSONDecodeError

POST_PATH = "posts.json"


def load_posts():
    try:
        with open(POST_PATH) as file:
            posts = json.load(file)
        return posts
    except JSONDecodeError:
        return "Файл не удается преобразовать"


def search_post(tag):
    posts_by_teg = []
    for post in load_posts():
        if tag.lower() in post['content'].lower():
            posts_by_teg.append(post)
    return posts_by_teg


def add_post(post):
    try:
        with open(POST_PATH) as file:
            data = json.load(file)
            data.append(post)
        with open(POST_PATH, "w") as fp:
            json.dump(data, fp, ensure_ascii=False)
    except FileNotFoundError:
        return "Файл не найден"
    except JSONDecodeError:
        return "Файл не удается преобразовать"

