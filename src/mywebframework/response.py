from pydantic import BaseModel


class Response(BaseModel, frozen=True):
    content: str
    status: int
