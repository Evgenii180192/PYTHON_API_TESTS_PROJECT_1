from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ModelRegisterUnsuccessful(BaseModel):
    error: str

    @field_validator('error')
    @classmethod
    def check_value_error_register_unsuccessful(cls, value_error):
        if value_error != "Missing password":
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


# "Converting model to json schema"
json_schema_register_unsuccessful = ModelRegisterUnsuccessful.model_json_schema()
