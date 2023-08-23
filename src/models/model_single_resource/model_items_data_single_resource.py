from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ItemsDataSingleResource(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str

    @field_validator('id')
    @classmethod
    def check_value_id_single_resource(cls, value_id):
        logger.info("Checking value id single resource")
        if value_id != 2:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


    @field_validator('year')
    @classmethod
    def check_value_year_single_resource(cls, value_year):
        logger.info("Checking value year single resource")
        if value_year != 2001:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)
