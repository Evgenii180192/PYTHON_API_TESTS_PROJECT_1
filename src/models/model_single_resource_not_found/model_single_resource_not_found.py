from loguru import logger
from pydantic import BaseModel


class ModelSingleResourceNotFound(BaseModel):
    pass


# "Converting model to json schema"
json_schema_single_resource_not_found = ModelSingleResourceNotFound.model_json_schema()
