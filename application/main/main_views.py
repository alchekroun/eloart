from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__, template_folder='templates', static_folder='static')


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/ranks')
def ranks():
    return render_template('ranks.html')


@main_bp.route('/fight')
def fight():
    return render_template('fight.html')