import unittest
import logging
from flask import jsonify

from app.app import app
from app.utils.logger_wrapper import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


class FlaskrTestCase(unittest.TestCase):
    API_PREFIX = '/v1'

    def setUp(self):
        logger.info('Setting up for the test suite')
        self.app = app.test_client()

    def tearDown(self):
        logger.info('Cleaning up')

    # Start tests

    def initialize_list(self):
        res = self.app.post(self.API_PREFIX +'/asset/sample', data="{\"assetType\":\"antenna\", \"assetClass\":\"dish\"}", content_type='application/json')

    def test_list_works(self):
        logger.info("test_list_works")
        res = self.app.get(self.API_PREFIX +'/assets')
        logger.info(res.data.decode('utf-8'))
        assert res.status_code == 200

    def test_get_asset(self):
        logger.info("test_get_asset")
        self.initialize_list()
        res = self.app.get(self.API_PREFIX +'/asset/sample')
        logger.info(res.data.decode('utf-8'))
        assert res.status_code == 200

    def test_no_body(self):
        logger.info("test_no_body")
        res = self.app.post(self.API_PREFIX +'/asset/nobody')
        logger.info(res.data.decode('utf-8'))
        assert res.status_code == 400

    def test_add_asset(self):
        logger.info("test_add_asset")
        res = self.app.post(self.API_PREFIX +'/asset/test', data="{\"assetType\":\"antenna\", \"assetClass\":\"dish\"}", content_type='application/json')
        logger.info(res.data.decode('utf-8'))
        assert res.status_code == 200

    def test_add_asset_invalid_name_start(self):
        logger.info("test_add_asset_invalid_name_start")
        res = self.app.post(self.API_PREFIX +'/asset/-test', data="{\"assetType\":\"antenna\", \"assetClass\":\"dish\"}", content_type='application/json')
        logger.info(res.data.decode('utf-8'))
        assert res.status_code == 400

    def test_add_asset_invalid_name_too_short(self):
        logger.info("test_add_asset_invalid_name_too_short")
        res = self.app.post(self.API_PREFIX +'/asset/t', data="{\"assetType\":\"antenna\", \"assetClass\":\"dove\"}", content_type='application/json')
        logger.info(res.data.decode('utf-8'))
        assert res.status_code == 400

    def test_add_asset_invalid_name_too_long(self):
        logger.info("test_add_asset_invalid_name_too_long")
        res = self.app.post(self.API_PREFIX +'/asset/eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee',
            data="{\"assetType\":\"antenna\", \"assetClass\":\"dove\"}", content_type='application/json')
        logger.info(res.data.decode('utf-8'))
        assert res.status_code == 400

    def test_add_asset_invalid_type(self):
        logger.info("test_add_asset_invalid_type")
        res = self.app.post(self.API_PREFIX +'/asset/test', data="{\"assetType\":\"blah\", \"assetClass\":\"dish\"}", content_type='application/json')
        logger.info(res.data.decode('utf-8'))
        assert res.status_code == 400

    def test_add_asset_invalid_class(self):
        logger.info("test_add_asset_invalid_class")
        res = self.app.post(self.API_PREFIX +'/asset/test', data="{\"assetType\":\"antenna\", \"assetClass\":\"dove\"}", content_type='application/json')
        logger.info(res.data.decode('utf-8'))
        assert res.status_code == 400

    def test_invalid_endpoint(self):
        logger.info("test_invalid_endpoint")
        res = self.app.post(self.API_PREFIX +"/hi")
        logger.info(res.data.decode('utf-8'))
        assert res.status_code == 404

if __name__ == '__main__':
    unittest.main()
