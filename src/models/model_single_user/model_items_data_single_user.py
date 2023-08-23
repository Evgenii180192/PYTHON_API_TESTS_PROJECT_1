from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ItemsDataSingleUser(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    @field_validator("id")
    @classmethod
    def check_value_id_single_user(cls, value):
        logger.info("Checking value id from single user")
        if value < 0:
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)

