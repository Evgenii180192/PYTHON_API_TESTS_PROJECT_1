from loguru import logger
from pydantic import BaseModel, field_validator
from pydantic.types import List

from src.models.model_delayed_response.model_items_data_delayed_response import ItemsDataDelayedResponse
from src.models.model_delayed_response.model_items_support_delayed_response import ItemsSupportDelayedResponse
from src.errors import ModelValueError


class ModelDelayedResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[ItemsDataDelayedResponse]
    support: ItemsSupportDelayedResponse

    @field_validator('total')
    @classmethod
    def check_value_total_delayed_response(cls, value_total):
        if value_total != 12:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)

    @field_validator('total_pages')
    @classmethod
    def check_value_total_pages_delayed_response(cls, value_total_pages):
        if value_total_pages != 2:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


# "Converting model to json schema"
json_schema_delayed_response = ModelDelayedResponse.model_json_schema()
