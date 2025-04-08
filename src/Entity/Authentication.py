from pydantic import BaseModel

class Authentication(BaseModel):
    connector: str
    token: str