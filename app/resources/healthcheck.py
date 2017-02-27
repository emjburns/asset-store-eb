import structlog

from flask_restful_swagger import swagger
from flask_restful import Resource

logger = structlog.get_logger(__name__)


class HealthCheck(Resource):
    @swagger.operation(
        notes='Checks health of the system',
        nickname='health-check',
        responseMessages=[
            {
                'code': 200,
                'Message': '{"healthy": True}'
            }
        ]
    )
    def get(self):
        # Logging
        logger.debug('debug')
        logger.info('info')
        logger.warning('warn')
        logger.error('error')
        logger.critical('critical')
        data = {'healthy': True}
        logger.info(data=data)
        return data
