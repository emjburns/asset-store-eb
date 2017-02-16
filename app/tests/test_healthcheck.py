import os, json
import unittest
import logging

from app.app import app
from app.utils.logger_wrapper import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        logger.info("Setting up for the test suite...")
        self.app = app.test_client()

    def tearDown(self):
        logger.info("Cleaning up...")

    # Begin Tests
    def test_healthcheck_works(self):
        res = self.app.get('/health-check')
        assert res.status_code == 200
        logger.info(res.data.decode("utf-8"))
