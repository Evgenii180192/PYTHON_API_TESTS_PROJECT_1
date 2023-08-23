from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ModelUpdatePatch(BaseModel):
    name: str
    job: str
    updatedAt: str

    @field_validator('name')
    @classmethod
    def check_value_name_update_patch(cls, value_name):
        if len(value_name) < 2:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)

    @field_validator('job')
    @classmethod
    def check_value_job_update_patch(cls, value_job):
        if len(value_job) < 2:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


# "Converting model to json schema"
json_schema_update_patch = ModelUpdatePatch.model_json_schema()
