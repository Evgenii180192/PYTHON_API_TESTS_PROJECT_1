from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_register_unsuccessful
from src.headers.headers_register_unsuccessful import headers_register_unsuccessful
from src.models.model_register_unsuccessful.model_register_unsuccessful import json_schema_register_unsuccessful
from src.models.model_register_unsuccessful.model_register_unsuccessful import ModelRegisterUnsuccessful

"""The module contains autotests for url = https://reqres.in/api/register"""


def test_validate_status_code_register_unsuccessful(request_register_unsuccessful):
    logger.info("Checking the status of the response code")
    BaseResponse(request_register_unsuccessful).validate_status_code(400)


def test_validate_json_schema_register_unsuccessful(request_register_unsuccessful):
    logger.info("JSON schema validation")
    BaseResponse(request_register_unsuccessful).validate_json_schema(json_schema_register_unsuccessful)


def test_validate_model_register_unsuccessful(request_register_unsuccessful):
    logger.info("Checking response data from model")
    BaseResponse(request_register_unsuccessful).validate_value_model(ModelRegisterUnsuccessful)


def test_validate_response_headers_register_unsuccessful(request_register_unsuccessful):
    logger.info("Checking response headers")
    BaseResponse(request_register_unsuccessful).validate_response_headers(headers_register_unsuccessful)
