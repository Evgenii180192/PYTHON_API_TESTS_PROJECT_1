from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_single_resource
from src.models.model_single_resource.model_single_resource import json_schema_single_resource
from src.models.model_single_resource.model_single_resource import ModelSingleResource
from src.headers.headers_single_resource import headers_single_resource

"""The module contains autotests for url = https://reqres.in/api/unknown/2"""


def test_validate_status_code_single_resource(request_single_resource):
    logger.info("Checking the status of the response code")
    BaseResponse(request_single_resource).validate_status_code(200)


def test_validate_json_schema_single_resource(request_single_resource):
    logger.info("JSON schema validation")
    BaseResponse(request_single_resource).validate_json_schema(json_schema_single_resource)


def test_validate_model_single_resource(request_single_resource):
    logger.info("Checking response data from model")
    BaseResponse(request_single_resource).validate_value_model(ModelSingleResource)


def test_validate_response_headers_single_resource(request_single_resource):
    logger.info("Checking response headers")
    BaseResponse(request_single_resource).validate_response_headers(headers_single_resource)
