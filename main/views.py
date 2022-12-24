from flask import Blueprint, render_template

main_blueprint = Blueprint('mane_blueprint', __name__)


@main_blueprint.route('/')
def page_index():
    return render_template('index.html')
