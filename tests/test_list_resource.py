from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_list_resource
from src.models.model_list_resource.model_list_resource import json_schema_list_resource
from src.models.model_list_resource.model_list_resource import ModelListResource
from src.headers.headers_list_resource import headers_list_resource

"""The module contains autotests for url = https://reqres.in/api/unknown"""


def test_validate_status_code_list_resource(request_list_resource):
    logger.info("Checking the status of the response code")
    BaseResponse(request_list_resource).validate_status_code(200)


def test_validate_json_schema_list_resource(request_list_resource):
    logger.info("JSON schema validation")
    BaseResponse(request_list_resource).validate_json_schema(json_schema_list_resource)


def test_validate_model_list_resource(request_list_resource):
    logger.info("Checking response data from model")
    BaseResponse(request_list_resource).validate_value_model(ModelListResource)


def test_validate_response_headers_list_resource(request_list_resource):
    logger.info("Checking response headers")
    BaseResponse(request_list_resource).validate_response_headers(headers_list_resource)
