"""REST API."""

import random

from flask_restful import Resource


class CoinToss(Resource):
    """Coin Toss result API."""

    def get(self):
        toss = bool(random.getrandbits(1))
        return {'result': toss}
