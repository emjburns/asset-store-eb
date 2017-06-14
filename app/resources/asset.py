import structlog
# import app.asset.AssetStore
# import app.asset.Asset

from flask_restful_swagger import swagger
from flask_restful import Resource

logger = structlog.get_logger(__name__)


class Asset(Resource):
    @swagger.operation(
        notes='Get a single asset',
        nickname='asset',
        responseMessages=[
            {
                'code': 200
            }
        ]
    )
    def get(self, name):
        # data = {'healthy': True}
        # return data

        return "I'm an asset with name: " + name

    @swagger.operation(
        notes='Create an asset',
        nickname='asset',
        responseMessages=[
            {
                'code': 200
            }
        ]
    )
    def post(self):
        return "You, my friend, have created an asset"
