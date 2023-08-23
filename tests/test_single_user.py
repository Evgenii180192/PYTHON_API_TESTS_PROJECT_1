from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_single_user
from src.models.model_single_user.model_single_user import json_schema_single_user
from src.headers.headers_single_user import headers_single_user
from src.models.model_single_user.model_single_user import ModelSingleUser

"""The module contains autotests for url = https://reqres.in/api/users/2"""


def test_validate_status_code_single_user(request_single_user):
    logger.info("Checking the status of the response code")
    BaseResponse(request_single_user).validate_status_code(200)


def test_validate_json_schema_single_user(request_single_user):
    logger.info("JSON schema validation")
    BaseResponse(request_single_user).validate_json_schema(json_schema_single_user)


def test_validate_model_single_user(request_single_user):
    logger.info("Checking response data from model")
    BaseResponse(request_single_user).validate_value_model(ModelSingleUser)


def test_validate_response_headers_single_user(request_single_user):
    logger.info("Checking response headers")
    BaseResponse(request_single_user).validate_response_headers(headers_single_user)
