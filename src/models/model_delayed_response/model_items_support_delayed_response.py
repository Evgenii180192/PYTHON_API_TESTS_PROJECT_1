from pydantic import BaseModel

class ItemsSupportDelayedResponse(BaseModel):
    url: str
    text: str
