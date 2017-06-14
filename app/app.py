from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger

from resources.assetsAPI import AssetsAPI
from resources.assetAPI import AssetAPI

app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1')

api.add_resource(AssetsAPI, '/v1/assets')
api.add_resource(AssetAPI, '/v1/asset/<string:name>')
