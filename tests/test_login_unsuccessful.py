from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_login_unsuccessful
from src.headers.headers_login_unsuccessful import headers_login_unsuccessful
from src.models.model_login_unsuccessful.model_login_unsuccessful import json_schema_login_unsuccessful
from src.models.model_login_unsuccessful.model_login_unsuccessful import ModelLoginUnsuccessful

"""The module contains autotests for url = https://reqres.in/api/login"""


def test_validate_status_code_login_unsuccessful(request_login_unsuccessful):
    logger.info("Checking the status of the response code")
    BaseResponse(request_login_unsuccessful).validate_status_code(400)


def test_validate_json_schema_login_unsuccessful(request_login_unsuccessful):
    logger.info("JSON schema validation")
    BaseResponse(request_login_unsuccessful).validate_json_schema(json_schema_login_unsuccessful)


def test_validate_model_login_unsuccessful(request_login_unsuccessful):
    logger.info("Checking response data from model")
    BaseResponse(request_login_unsuccessful).validate_value_model(ModelLoginUnsuccessful)


def test_validate_response_headers_login_unsuccessful(request_login_unsuccessful):
    logger.info("Checking response headers")
    BaseResponse(request_login_unsuccessful).validate_response_headers(headers_login_unsuccessful)
