from pydantic import BaseModel
from src.models.model_single_resource.model_items_data_single_resource import ItemsDataSingleResource
from src.models.model_single_resource.model_items_support_single_resource import ItemsSupportSingleResource


class ModelSingleResource(BaseModel):
    data: ItemsDataSingleResource
    support: ItemsSupportSingleResource


# "Converting model to json schema"
json_schema_single_resource = ModelSingleResource.model_json_schema()
