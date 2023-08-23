from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ModelUpdate(BaseModel):
    name: str
    job: str
    updatedAt: str

    @field_validator('name')
    @classmethod
    def check_value_name_update(cls, value_name):
        logger.info('Checking value name from update')
        if len(value_name) < 2 and not isinstance(value_name, str):
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)

    @field_validator('job')
    @classmethod
    def check_value_job_update(cls, value_job):
        logger.info('Checking value job from update')
        if len(value_job) < 2 and not isinstance(value_job, str):
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


# "Converting model to json schema"
json_schema_update = ModelUpdate.model_json_schema()
