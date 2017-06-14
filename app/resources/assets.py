import structlog
# import app.asset.AssetStore
# import app.asset.Asset

from flask_restful_swagger import swagger
from flask_restful import Resource

logger = structlog.get_logger(__name__)


class Assets(Resource):
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
        # Logging
        # logger.debug('debug')
        # logger.info('info')
        # logger.warning('warn')
        # logger.error('error')
        # logger.critical('critical')
        # data = {'healthy': True}
        # logger.info(data=data)

        return "TEST"
