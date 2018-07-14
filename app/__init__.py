"""Main application initialisation."""

from flask import Flask
from flask_restful import Api
from app.api import CoinToss
from app.views import index


def create_app():
    app = Flask(__name__)
    api = Api(app)

    # App API Resources here
    api.add_resource(CoinToss, '/api/v1/cointoss')

    # Add app URL Routes
    app.add_url_rule('/', 'index', index)

    return app
