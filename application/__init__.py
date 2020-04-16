from flask import Flask
from flask_session import Session
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy

sess = Session()
mysql = MySQL()
db = SQLAlchemy()


def create_app():
    """Construct the core app object"""
    app = Flask(__name__, instance_relative_config=False)

    # config
    app.config.from_object('config.Config')

    # init
    mysql.init_app(app)
    db.init_app(app)

    with app.app_context():
        # Include Routes
        from .main import main_views
        app.register_blueprint(main_views.main_bp)

    return app
