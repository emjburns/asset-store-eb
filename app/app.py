from flask import Flask
from flask_restful import (
    Api,
)
from flask_restful_swagger import swagger

from resources.assets import Assets
from resources.asset import Asset
# from assets.assetStore import AssetStore

# Declare name of app object and create an instance as an API
app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1')

# list all assets (GET)
api.add_resource(Assets, '/assets')
# create (POST) and find (GET) asset
api.add_resource(Asset, '/asset/<string:name>')
