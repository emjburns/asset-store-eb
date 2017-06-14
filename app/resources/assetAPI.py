import structlog
from app.asset.assetStore import *
from app.asset.asset import *

from flask import abort
from flask import jsonify
from flask_restful_swagger import swagger
from flask_restful import Resource
from flask_restful import reqparse

logger = structlog.get_logger(__name__)


class AssetAPI(Resource):
    assets = AssetStore()

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('assetType', type = str, required = True,
            help = 'No assetType provided', location = 'json')
        self.reqparse.add_argument('assetClass', type = str, required = True,
            help = 'No assetClass provided', location = 'json')
        super(AssetAPI, self).__init__()

    def api_response(self, code, message):
        response = jsonify({'message': message})
        response.status_code = code
        return response

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
        asset = self.assets.getAsset(name)
        if (asset == None):
            return self.api_response(404, "Asset not found")
        return asset.serialize()


    @swagger.operation(
        notes='Create an asset',
        nickname='asset',
        parameters=[
            {
              "name": "body",
              "description": "Json list of parameters containing 'assetType' and 'assetClass'. \
              For 'assetType', either 'satellite' or 'antenna' is valid. \
              For an 'assetType' of 'satelite', an 'assetClass' of 'dove' or 'rapideye' is valid. \
              For an 'assetType' of 'antenna', an 'assetClass' of 'dish' or 'yagi' is valid. \
              Example: {\"assetType\":\"satellite\", \"assetClass\":\"dove\"}",
              "required": True,
              "allowMultiple": False,
              "dataType": "string",
              "paramType": "body"
            },
          ],
        responseMessages=[
            {
                'code': 200
            }
        ]
    )
    def post(self, name):
        args = self.reqparse.parse_args()
        # Parser insures they exist
        assetType = args["assetType"]
        assetClass = args["assetClass"]
        myasset = Asset(name, assetType, assetClass)
        valid, message = myasset.validateAsset()
        if (not valid):
            return self.api_response(400, "Asset not valid. " + message )

        success = self.assets.addAsset(myasset)
        if (not success):
            return self.api_response(400, "Asset already exists.")
        return jsonify(myasset.serialize())
