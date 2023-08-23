from pydantic import BaseModel, field_validator
from src.errors import ModelValueError


class ModelLogin(BaseModel):
    token: str

    @field_validator('token')
    @classmethod
    def check_value_token_login(cls, value_token):
        if not isinstance(value_token, str):
            raise ValueError(ModelValueError.MODEL_VALUE_ERROR.value)


# "Converting model to json schema"
json_schema_login = ModelLogin.model_json_schema()
