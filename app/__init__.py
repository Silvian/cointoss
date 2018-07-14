"""Main application initialisation."""

from flask import Flask
from flask_restful import Api
from app.api import CoinToss


def create_app():
    app = Flask(__name__)
    api = Api(app)

    # App API Resources here
    api.add_resource(CoinToss, '/api/v1/cointoss')

    return app
