from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ModelRegister(BaseModel):
    id: int
    token: str


    @field_validator('id')
    @classmethod
    def check_value_id_register(cls, value_id):
        if value_id < 1:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


# "Converting model to json schema"
json_schema_register = ModelRegister.model_json_schema()
