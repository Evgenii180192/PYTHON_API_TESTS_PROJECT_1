from loguru import logger
from src.base_response import BaseResponse
from src.conftest import request_list_users
from src.headers.headers_list_users import headers_list_users
from src.models.model_list_users.model_list_users import json_schema_list_users
from src.models.model_list_users.model_list_users import ModelListUsers

"""The module contains autotests for url = https://reqres.in/api/users?page=2"""


def test_validate_status_code_list_users(request_list_users):
    logger.info("Checking the status of the response code")
    BaseResponse(request_list_users).validate_status_code(200)


def test_validate_json_schema_list_users(request_list_users):
    logger.info("JSON schema validation")
    BaseResponse(request_list_users).validate_json_schema(json_schema_list_users)


def test_validate_model_list_users(request_list_users):
    logger.info("Checking response data from model")
    BaseResponse(request_list_users).validate_value_model(ModelListUsers)


def test_validate_response_headers_list_users(request_list_users):
    logger.info("Checking response headers")
    BaseResponse(request_list_users).validate_response_headers(headers_list_users)
