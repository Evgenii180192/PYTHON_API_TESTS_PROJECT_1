from jsonschema import validate
from loguru import logger
from requests import JSONDecodeError

from src.errors import StatusCodeError, JSONSchemaError, ModelValueError, ResponseHeadersError


class BaseResponse:
    def __init__(self, response):
        """Initializing the response from the server"""
        self.response = response
        try:
            self.response_json = response.json()
        except JSONDecodeError:
            logger.info("No Content")
        self.response_status_code = response.status_code
        logger.info(response.status_code)
        self.response_headers = response.headers
        request_time = self.response_elapsed = response.elapsed
        logger.info(f"Request time: {request_time}")

    def validate_status_code(self, status_code):
        """The method for checking response code status"""
        assert self.response_status_code == status_code, StatusCodeError.STATUS_CODE_ERROR
        return self

    def validate_json_schema(self, schema):
        """The method check json - schema from response"""
        if isinstance(self.response_json, list):
            for item in self.response.json:
                validate(item, schema), JSONSchemaError.JSON_SCHEMA_ERROR.value
        else:
            validate(self.response_json, schema), JSONSchemaError.JSON_SCHEMA_ERROR
        return self

    def validate_value_model(self, model):
        """The method to validate values from response"""
        if isinstance(self.response_json, list):
            for item in self.response_json:
                model.model_validate(item), ModelValueError.MODEL_VALUE_ERROR
        else:
            model.model_validate(self.response_json), ModelValueError.MODEL_VALUE_ERROR
        return self

    def validate_response_headers(self, list_headers):
        """The method for checking headers from response"""
        for i in self.response_headers:
            if i not in list_headers:
                raise ValueError(ResponseHeadersError.Response_HEADERS_ERRORS)
        return self
