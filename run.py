import os

# Setup all the logging before importing the app.
from app.utils.logger_wrapper import setup_logging
setup_logging()  # Set up logging before importing the app
from app.app import app
import structlog

logger = structlog.get_logger(__name__)


if __name__ == '__main__':
    app.debug = True if os.getenv(
        'APP_DEBUG', 'false').lower() == 'true' else False
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    logger.info("Service starting up", url="http://%s:%d" % (host, port))
    app.run(host=host, port=port, processes=1)
