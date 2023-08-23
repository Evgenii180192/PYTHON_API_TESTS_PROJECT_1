from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_register
from src.headers.headers_register import headers_register
from src.models.model_register.model_register import json_schema_register, ModelRegister

"""The module contains autotests for url = https://reqres.in/api/register"""


def test_validate_status_code_register(request_register):
    logger.info("Checking the status of the response code")
    BaseResponse(request_register).validate_status_code(200)


def test_validate_json_schema_register(request_register):
    logger.info("JSON schema validation")
    BaseResponse(request_register).validate_json_schema(json_schema_register)


def test_validate_model_register(request_register):
    logger.info("Checking response data from model")
    BaseResponse(request_register).validate_value_model(ModelRegister)


def test_validate_response_headers_register(request_register):
    logger.info("Checking response headers")
    BaseResponse(request_register).validate_response_headers(headers_register)