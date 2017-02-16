import os

#Setup all the logging before importing the app.
from app.utils.logger_wrapper import setup_logging
setup_logging()

from app.app import app

if __name__ == '__main__':
    app.debug = True if os.getenv('APP_DEBUG', 'false').lower() == 'true' else False
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, processes=1)
