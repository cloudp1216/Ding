

from flask import Flask
from .views import root


APP_NAME = 'ding_proxy'


def create_app():
    app = Flask(APP_NAME)

    register_blueprints(app)

    return app
    

def register_blueprints(app):
    app.register_blueprint(root, url_prefix='/')


