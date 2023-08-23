from enum import Enum

"""The module contains errors that occur when checking the response from the server"""


class StatusCodeError(Enum):
    STATUS_CODE_ERROR = 'Status code is different than expected'


class JSONSchemaError(Enum):
    JSON_SCHEMA_ERROR = 'JSON-Scheme does not match expected result'


class ModelValueError(Enum):
    MODEL_VALUE_ERROR = 'Value does not match expected'


class ResponseHeadersError(Enum):
    Response_HEADERS_ERRORS = 'Response does not contain this header'


class TimeoutResponseError(Enum):
    TIMEOUT_Response_ERROR = 'Timed out waiting for a response from the server'
