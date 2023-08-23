from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_update_patch
from src.headers.headers_update_patch import headers_update_patch
from src.models.model_update_patch.model_update_patch import json_schema_update_patch
from src.models.model_update_patch.model_update_patch import ModelUpdatePatch

"""The module contains autotests for url = https://reqres.in/api/users/2"""


def test_validate_status_code_update_patch(request_update_patch):
    logger.info("Checking the status of the response code")
    BaseResponse(request_update_patch).validate_status_code(200)


def test_validate_json_schema_update_patch(request_update_patch):
    logger.info("JSON schema validation")
    BaseResponse(request_update_patch).validate_json_schema(json_schema_update_patch)


def test_validate_model_update_patch(request_update_patch):
    logger.info("Checking response data from model")
    BaseResponse(request_update_patch).validate_value_model(ModelUpdatePatch)


def test_validate_response_headers_update_patch(request_update_patch):
    logger.info("Checking response headers")
    BaseResponse(request_update_patch).validate_response_headers(headers_update_patch)
