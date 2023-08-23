from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_delayed_response
from src.headers.headers_delayed_response import headers_delayed_response
from src.models.model_delayed_response.model_delayed_response import json_schema_delayed_response
from src.models.model_delayed_response.model_delayed_response import ModelDelayedResponse

"""The module contains autotests for url = https://reqres.in/api/login"""


def test_validate_status_code_delayed_response(request_delayed_response):
    logger.info("Checking the status of the response code")
    BaseResponse(request_delayed_response).validate_status_code(200)


def test_validate_json_schema_delayed_response(request_delayed_response):
    logger.info("JSON schema validation")
    BaseResponse(request_delayed_response).validate_json_schema(json_schema_delayed_response)


def test_validate_model_delayed_response(request_delayed_response):
    logger.info("Checking response data from model")
    BaseResponse(request_delayed_response).validate_value_model(ModelDelayedResponse)


def test_validate_response_headers_delayed_response(request_delayed_response):
    logger.info("Checking response headers")
    BaseResponse(request_delayed_response).validate_response_headers(headers_delayed_response)