from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ModelLoginUnsuccessful(BaseModel):
    error: str

    @classmethod
    def check_value_error_login_unsuccessful(cls, value_token):
        if value_token != "Missing password":
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


# "Converting model to json schema"
json_schema_login_unsuccessful = ModelLoginUnsuccessful.model_json_schema()