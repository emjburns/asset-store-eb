import structlog
from app.asset.assetStore import *
from app.asset.asset import *

from flask_restful_swagger import swagger
from flask_restful import Resource
from flask import jsonify

logger = structlog.get_logger(__name__)


class AssetsAPI(Resource):

    assets = AssetStore()
    
    @swagger.operation(
        notes='Get all assets',
        nickname='assets',
        responseMessages=[
            {
                'code': 200
            }
        ]
    )
    def get(self):
        return jsonify(assets=[a.serialize() for a in self.assets.getAll()])
