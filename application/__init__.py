from flask import Flask
from flask_session import Session

sess = Session()


def create_app():
    """Construct the core app object"""
    app = Flask(__name__, instance_relative_config=False)

    # config
    app.config.from_object('config.Config')

    # init

    with app.app_context():
        # Include Routes
        from .main import main_views
        app.register_blueprint(main_views.main_bp)

    return app
