from pydantic import BaseModel
from typing import Union

class DirectMessage(BaseModel):
    apiKey: Union[str, None] = None
    apiSecret: Union[str, None] = None
    accessToken: str
    accessSecret: Union[str, None] = None
    userId: Union[str, None] = None
