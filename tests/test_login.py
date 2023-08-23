from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_login
from src.headers.headers_login import headers_login
from src.models.model_login.model_login import json_schema_login
from src.models.model_login.model_login import ModelLogin


"""The module contains autotests for url = https://reqres.in/api/login"""



def test_validate_status_code_login(request_login):
    logger.info("Checking the status of the response code")
    BaseResponse(request_login).validate_status_code(200)


def test_validate_json_schema_login(request_login):
    logger.info("JSON schema validation")
    BaseResponse(request_login).validate_json_schema(json_schema_login)


def test_validate_model_login(request_login):
    logger.info("Checking response data from model")
    BaseResponse(request_login).validate_value_model(ModelLogin)


def test_validate_response_headers_login(request_login):
    logger.info("Checking response headers")
    BaseResponse(request_login).validate_response_headers(headers_login)