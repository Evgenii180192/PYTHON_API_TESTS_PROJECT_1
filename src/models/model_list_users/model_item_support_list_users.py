from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ItemSupport(BaseModel):
    url: str
    text: str

    @field_validator("text")
    @classmethod
    def check_value_text_list_users(cls, value_text):
        logger.info("Checking value text from list users")
        if value_text != "To keep ReqRes free, contributions towards server costs are appreciated!":
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)
