from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_single_resource_not_found
from src.models.model_single_resource_not_found.model_single_resource_not_found import (
    json_schema_single_resource_not_found)
from src.models.model_single_resource_not_found.model_single_resource_not_found import ModelSingleResourceNotFound
from src.headers.headers_single_resource_not_found import headers_single_resource_not_found


"""The module contains autotests for url = https://reqres.in/api/unknown/23"""


def test_validate_status_code_single_resource_not_found(request_single_resource_not_found):
    logger.info("Checking the status of the response code")
    BaseResponse(request_single_resource_not_found).validate_status_code(404)


def test_validate_json_schema_single_resource_not_found(request_single_resource_not_found):
    logger.info("JSON schema validation")
    BaseResponse(request_single_resource_not_found).validate_json_schema(json_schema_single_resource_not_found)


def test_validate_model_single_resource_not_found(request_single_resource_not_found):
    logger.info("Checking response data from model")
    BaseResponse(request_single_resource_not_found).validate_value_model(ModelSingleResourceNotFound)


def test_validate_response_headers_single_resource_not_found(request_single_resource_not_found):
    logger.info("Checking response headers")
    BaseResponse(request_single_resource_not_found).validate_response_headers(headers_single_resource_not_found)


