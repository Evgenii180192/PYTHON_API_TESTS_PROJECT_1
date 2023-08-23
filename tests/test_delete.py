from loguru import logger

from src.base_response import BaseResponse
from src.conftest import request_delete
from src.headers.headers_delete import headers_delete

"""The module contains autotests for url = https://reqres.in/api/users/2"""


def test_validate_status_code_delete(request_delete):
    logger.info("Checking the status of the response code")
    BaseResponse(request_delete).validate_status_code(204)


def test_validate_response_headers_delete(request_delete):
    logger.info("Checking response headers")
    BaseResponse(request_delete).validate_response_headers(headers_delete)
