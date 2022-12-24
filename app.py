from flask import Flask, request, render_template, send_from_directory
import logging
from functions import add_post
from main.views import main_blueprint
from loader.views import loader_blueprint

UPLOAD_FOLDER = "./uploads/images/"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

logging.basicConfig(filename="basic.log", level=logging.INFO)

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/post", methods=["GET"])
def page_post_form():
    return render_template('post_form.html')


@app.route("/post", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    if picture:
        filename = picture.filename
        extension = filename.split(".")[-1]
        if extension in ALLOWED_EXTENSIONS:
            picture.save(f'{UPLOAD_FOLDER}{filename}')
            post = {"pic": f"{UPLOAD_FOLDER}{filename}", "content": request.form["content"]}
            add_post(post)
            return render_template('post_uploaded.html', text_post=post["content"], url=post["pic"])
        else:
            logging.info(f"Попытка загрузки файла с расширением {extension}")
            return render_template("mistake.html", extension=extension)
    else:
        logging.error("Ошибка загрузки файла")
        return "Файл не загружен"


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
