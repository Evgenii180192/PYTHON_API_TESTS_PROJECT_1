from pydantic import BaseModel

class ItemsDataDelayedResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str






