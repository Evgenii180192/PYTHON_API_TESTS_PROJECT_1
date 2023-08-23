from loguru import logger
from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ItemsSupportSingleUser(BaseModel):
    url: str
    text: str


    @field_validator('url')
    @classmethod
    def check_value_url_single_user(cls, value_url):
        logger.info("Checking value url from single user")
        if value_url != "https://reqres.in/#support-heading":
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


    @field_validator('text')
    @classmethod
    def check_value_text_single_user(cls, value_text):
        logger.info("Checking value text from single user")
        if value_text != "To keep ReqRes free, contributions towards server costs are appreciated!":
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


