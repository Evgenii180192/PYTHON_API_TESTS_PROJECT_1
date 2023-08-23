from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ItemDataListUsers(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    @field_validator('id')
    @classmethod
    def check_value_id_list_users(cls, value_id):
        logger.info("Checking value id from list users")
        if value_id < 0:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)

    @field_validator('email')
    @classmethod
    def check_value_email_list_users(cls, value_email):
        logger.info("Checking value email from list users")
        if '@' not in value_email:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)

    @field_validator('first_name')
    @classmethod
    def check_value_first_name_list_users(cls, value_first_name):
        logger.info("Checking value first_name from list users")
        if len(value_first_name) < 2:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)

    @field_validator('last_name')
    @classmethod
    def check_value_last_name_list_users(cls, value_last_name):
        logger.info("Checking value last_name from list users")
        if len(value_last_name) < 2:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)
