from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_create
from src.models.model_create.model_create import json_schema_create
from src.models.model_create.model_create import ModelCreate
from src.headers.headers_create import headers_create

"""The module contains autotests for url = https://reqres.in/api/users"""


def test_validate_status_code_create(request_create):
    logger.info("Checking the status of the response code")
    BaseResponse(request_create).validate_status_code(201)


def test_validate_json_schema_create(request_create):
    logger.info("JSON schema validation")
    BaseResponse(request_create).validate_json_schema(json_schema_create)


def test_validate_model_create(request_create):
    logger.info("Checking response data from model")
    BaseResponse(request_create).validate_value_model(ModelCreate)


def test_validate_response_headers_create(request_create):
    logger.info("Checking response headers")
    BaseResponse(request_create).validate_response_headers(headers_create)
