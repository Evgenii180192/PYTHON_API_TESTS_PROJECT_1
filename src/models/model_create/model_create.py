from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ModelCreate(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str


    @field_validator('name')
    @classmethod
    def check_value_name_create(cls, value_name):
        logger.info('Checking value name from create')
        if len(value_name) < 2:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


    @field_validator('job')
    @classmethod
    def check_value_job_create(cls, value_job):
        logger.info('Checking value job from create')
        if len(value_job) < 2 and not isinstance(value_job, str):
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)



    @field_validator('id')
    @classmethod
    def check_value_id_create(cls, value_id):
        logger.info('Checking value id from create')
        if int(value_id) <= 0:
            print(value_id)
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


# Converting model to json schema
json_schema_create = ModelCreate.model_json_schema()
