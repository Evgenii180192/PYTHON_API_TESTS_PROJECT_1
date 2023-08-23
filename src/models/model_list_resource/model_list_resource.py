from loguru import logger
from pydantic import BaseModel, field_validator
from pydantic.types import List
from src.models.model_list_resource.model_items_data_list_resource import ItemsDateListResource
from src.models.model_list_resource.model_items_support_list_resource import ItemsSupportListResource
from src.errors import ModelValueError


class ModelListResource(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[ItemsDateListResource]
    support: ItemsSupportListResource

    @field_validator('total')
    @classmethod
    def check_value_total_list_resource(cls, value_total):
        logger.info("Checking value total from list resource")
        if value_total != 12:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)

    @field_validator('total_pages')
    @classmethod
    def check_value_total_pages_list_resource(cls, value_total_pages):
        logger.info("Checking value total_pages from list resource")
        if value_total_pages != 2:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


# "Converting model to json schema"
json_schema_list_resource = ModelListResource.model_json_schema()
