from pydantic import BaseModel
from src.models.model_single_user.model_items_data_single_user import ItemsDataSingleUser
from src.models.model_single_user.model_items_support_single_user import ItemsSupportSingleUser


class ModelSingleUser(BaseModel):
    data: ItemsDataSingleUser
    support: ItemsSupportSingleUser


# "Converting model to json schema"
json_schema_single_user = ModelSingleUser.model_json_schema()
