from flask import Flask
from flask_restful import (
    Api,
)
from flask_restful_swagger import swagger

from app.resources.healthcheck import HealthCheck

# Declare name of app object and create an instance as an API
app = Flask(__name__)
api = swagger.docs(Api(app), apiVersion='0.1')

# Set up all your rest resources
api.add_resource(HealthCheck, '/health-check')
