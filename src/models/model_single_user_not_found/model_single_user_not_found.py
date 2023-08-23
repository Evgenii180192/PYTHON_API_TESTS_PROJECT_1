from loguru import logger
from pydantic import BaseModel


class SingleUserNotFound(BaseModel):
    pass


# "Converting model to json schema"
json_schema_single_not_found = SingleUserNotFound.model_json_schema()
