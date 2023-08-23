from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ItemsDateListResource(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str



    @field_validator('id')
    @classmethod
    def check_value_id_list_resource(cls, value_id):
        logger.info("Checking value id from list resource")
        if value_id < 0:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


    @field_validator('name')
    @classmethod
    def check_value_name_list_resource(cls, value_name):
        logger.info("Checking value name from list resource")
        if len(value_name) < 2:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)
