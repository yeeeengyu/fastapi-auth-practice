from pydantic import BaseModel
class Request(BaseModel):
    user: str
    password: str
    