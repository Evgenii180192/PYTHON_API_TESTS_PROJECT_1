from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_update
from src.headers.headers_update import headers_update
from src.models.model_update.model_update import json_schema_update
from src.models.model_update.model_update import ModelUpdate

"""The module contains autotests for url = https://reqres.in/api/users/2"""


def test_validate_status_code_update(request_update):
    logger.info("Checking the status of the response code")
    BaseResponse(request_update).validate_status_code(200)


def test_validate_json_schema_update(request_update):
    logger.info("JSON schema validation")
    BaseResponse(request_update).validate_json_schema(json_schema_update)


def test_validate_model_update(request_update):
    logger.info("Checking response data from model")
    BaseResponse(request_update).validate_value_model(ModelUpdate)


def test_validate_response_headers_update(request_update):
    logger.info("Checking response headers")
    BaseResponse(request_update).validate_response_headers(headers_update)
