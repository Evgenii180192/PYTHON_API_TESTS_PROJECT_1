from loguru import logger
from pydantic import BaseModel, field_validator
from typing import List
from src.models.model_list_users.model_item_data_list_users import ItemDataListUsers
from src.models.model_list_users.model_item_support_list_users import ItemSupport
from src.errors import ModelValueError


class ModelListUsers(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[ItemDataListUsers]
    support: ItemSupport

    @field_validator('page')
    @classmethod
    def check_value_page_list_users(cls, value_page):
        logger.info("Checking value page from list users")
        if value_page != 2:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)

    @field_validator('per_page')
    @classmethod
    def check_value_per_page_list_users(cls, value_per_page):
        logger.info("Checking value per_page from list users")
        if value_per_page != 6:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)

    @field_validator('total')
    @classmethod
    def check_value_total_list_users(cls, value_total):
        logger.info("Checking value total from list users")
        if value_total != 12:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)

    @field_validator('total_pages')
    @classmethod
    def check_value_total_pages_list_users(cls, value_total_pages):
        logger.info("Checking value total pages from list users")
        if value_total_pages != 2:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


# "Converting model to json schema"
json_schema_list_users = ModelListUsers.model_json_schema()

